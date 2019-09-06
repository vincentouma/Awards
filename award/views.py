from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http  import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import  *
from .models import *
# Create your views here.

def home(request):
   
    return render(request, 'home.html',
    )


def new_projects(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.profile = profile
            project.save()
        return redirect('index')

    else:
        form = ProjectsForm()
    return render(request, 'new_project.html', {"form": form})
