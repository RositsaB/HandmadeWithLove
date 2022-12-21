from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from handmade.accounts.models import Profile
from handmade.web.models import Project

UserModel = get_user_model()


class CreateProfileForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
        initial=Profile.DO_NOT_SHOW,
    )
    date_of_birth = forms.DateField()

    picture = forms.URLField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            gender=self.cleaned_data['gender'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            picture=self.cleaned_data['picture'],
            user=user)

        if commit:
            profile.save()
            return user

    class Meta:
        model = UserModel
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name',
                  'gender', 'date_of_birth', 'picture']


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        exclude = ['email', 'user']


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        Project.objects.filter(user_id=self.instance.id).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = UserModel
        fields = ()
