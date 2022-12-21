from django import forms

from handmade.web.models import Project, Comment, News


class CreateProjectForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        project = super().save(commit=False)
        project.user = self.user
        if commit:
            project.save()
        return project

    class Meta:
        model = Project
        fields = ('name', 'description', 'photo')


class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'photo',)


class DeleteProjectForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Project
        fields = ()


class AddCommentForm(forms.ModelForm):
    def __init__(self, user, project_id, author_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.project_id = project_id
        self.author_name = author_name

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.user = self.user
        comment.project_id = self.project_id
        comment.author_name = self.author_name
        if commit:
            comment.save()
        return comment

    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2}), label=''
        )

    class Meta:
        model = Comment
        fields = ['content']


class EditCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'body': forms.Textarea(
                attrs={'rows': 3}
            )
        }


class DeleteCommentForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Comment
        fields = ()


class CreateNewsForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        news = super().save(commit=False)
        news.user = self.user
        if commit:
            news.save()
        return news

    class Meta:
        model = News
        fields = ('title', 'content', 'picture')
