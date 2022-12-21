from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from handmade.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from handmade.accounts.models import Profile
from handmade.web.models import Project

UserModel = get_user_model()


class CreateProfileView(CreateView):
    template_name = 'accounts/profile_create.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('projects')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def form_valid(self, form):
        form.save()
        user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
        login(self.request, user)
        return redirect(reverse_lazy('projects'))


class LoginProfileView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('projects')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class DetailsProfileView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile_details.html'
    model = Profile
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        projects = Project.objects.filter(user_id=self.object.user)
        context['projects'] = projects
        context['is_owner'] = self.object.user == self.request.user
        return context


class EditProfileView(UpdateView):
    model = Profile
    template_name = 'accounts/profile_edit.html'
    form_class = EditProfileForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.user_id})


class DeleteProfileView(DeleteView):
    model = UserModel
    template_name = 'accounts/profile_delete.html'
    form_class = DeleteProfileForm
    success_url = reverse_lazy('index')
