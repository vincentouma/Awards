from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        # model = Profile
        exclude = ('profile_pic','bio',)

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ('website',)

class Votess(forms.Form):
    design = forms.CharField(label='Design level', widget=forms.RadioSelect)

    usability = forms.CharField(label='Usability level', widget=forms.RadioSelect)

    creativity  = forms.CharField(label='Creativity level', widget=forms.RadioSelect)

    content = forms.CharField(label='Content level', widget=forms.RadioSelect)
