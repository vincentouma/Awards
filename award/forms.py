from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Project,Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['prof_user','profile_Id']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','user_project_id']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('design','usability','content')
