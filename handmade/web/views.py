from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from handmade.accounts.models import Profile
from handmade.web.forms import CreateProjectForm, EditProjectForm, DeleteProjectForm, AddCommentForm, EditCommentForm, \
    DeleteCommentForm, CreateNewsForm
from handmade.web.models import Project, Comment, Favourites, News


def index(request):
    return render(request, 'web/index.html')


class ProjectsView(ListView):
    template_name = 'web/projects.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data()
        projects = Project.objects.all().order_by('-date_of_publication')
        context['projects'] = projects
        return context


class ProjectDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'web/project_details.html'
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['full_name'] = Profile.objects.get(user_id=self.object.user_id)
        fav_project_list = Project.objects.filter(favourites__user=self.request.user)
        context['favourites_list'] = fav_project_list
        context['comments'] = Comment.objects.filter(project_id=self.object.id)
        context['is_owner'] = self.object.user == self.request.user
        return context


class ProjectAddView(LoginRequiredMixin, CreateView):
    template_name = 'web/project_add.html'
    form_class = CreateProjectForm
    success_url = reverse_lazy('projects')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ProjectEditView(UpdateView):
    template_name = 'web/project_edit.html'
    form_class = EditProjectForm
    model = Project

    def get_success_url(self):
        return reverse_lazy('project details', kwargs={'pk': self.object.id})


class ProjectDeleteView(DeleteView):
    template_name = 'web/project_delete.html'
    model = Project
    form_class = DeleteProjectForm
    success_url = reverse_lazy('projects')


class CommentAddView(LoginRequiredMixin, CreateView):
    template_name = 'web/comment_add.html'
    model = Comment
    form_class = AddCommentForm

    def get_success_url(self):
        return reverse_lazy('project details', kwargs={'pk': self.object.project_id})

    def get_form_kwargs(self):
        author_name = Profile.objects.get(user_id=self.request.user)
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['project_id'] = self.kwargs['pk']
        kwargs['author_name'] = author_name
        return kwargs


class CommentEditView(LoginRequiredMixin, UpdateView):
    template_name = 'web/comment_edit.html'
    model = Comment
    form_class = EditCommentForm

    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        return reverse_lazy('project details', kwargs={'pk': self.object.project_id})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'web/comment_delete.html'
    form_class = DeleteCommentForm
    model = Comment

    def get_success_url(self):
        project_id = self.object.project_id
        return reverse_lazy('project details', kwargs={'pk': project_id})

    def get_context_data(self, **kwargs):
        context = super(CommentDeleteView, self).get_context_data()
        context['comment'] = Comment.objects.get(id=self.object.id)
        return context


class FavouritesAddView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        favourites = Favourites()
        favourites.project = Project.objects.get(pk=self.kwargs.get('pk'))
        favourites.user = self.request.user
        favourites.save()
        return redirect('favourites')


class FavouritesRemoveView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        favourites = Favourites()
        favourites.project = Project.objects.get(pk=self.kwargs.get('pk'))
        favourites.user = self.request.user
        fav_obj = Favourites.objects.filter(project_id=favourites.project)
        fav_obj.delete()
        return redirect('favourites')


class FavouritesView(ListView):
    template_name = 'web/favourites.html'
    model = Favourites
    context_object_name = 'favourites'

    def get_context_data(self, **kwargs):
        context = super(FavouritesView, self).get_context_data()
        context['favourites_list'] = Favourites.objects.filter(user=self.request.user)
        return context


class HandmadeNewsView(ListView):
    template_name = 'web/news.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super(HandmadeNewsView, self).get_context_data()
        news = News.objects.all()
        context['news'] = news
        return context


class HandmadeNewsAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'web.add_news'
    template_name = 'web/news_add.html'
    form_class = CreateNewsForm
    success_url = reverse_lazy('news')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


