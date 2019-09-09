from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from tinymce.models import HTMLField
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProjectForm,ProfileForm,VoteForm 
from .models import *
# Create your views here.

def home(request):
    current_user = request.user
    all_projects = Project.fetch_all_images()
    return render(request,"home.html",{"all_images":all_projects})
    
@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.prof_user = current_user
            profile.profile_Id = request.user.id
            profile.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/new_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        logged_user = Profile.objects.get(prof_user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=logged_user)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request,'profile/edit_profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Projects.objects.filter(user = current_user)

    try:   
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile/profile.html',{'profile':prof,'projects':projects})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            user_image = form.save(commit=False)
            user_image.user = current_user
            user_image.save()
        return redirect('home')
    else:
        form = ProjectForm()
    return render(request,"project.html",{"form":form})

@login_required(login_url='/accounts/login/')
def project_review(request,project_id):
    try:
        single_project = Project.get_single_project(project_id)
        average_score = round(((single_project.design + single_project.usability + single_project.content)/3),2)
        if request.method == 'POST':
            vote_form = VoteForm(request.POST)
            if vote_form.is_valid():
                single_project.vote_submissions+=1
                if single_project.design == 0:
                    single_project.design = int(request.POST['design'])
                else:
                    single_project.design = (single_project.design + int(request.POST['design']))/2
                if single_project.usability == 0:
                    single_project.usability = int(request.POST['usability'])
                else:
                    single_project.usability = (single_project.usability + int(request.POST['usability']))/2
                if single_project.content == 0:
                    single_project.content = int(request.POST['content'])
                else:
                    single_project.content = (single_project.content + int(request.POST['usability']))/2

                single_project.save()
                return redirect('project_review',project_id)
        else:
            vote_form = VoteForm()

    except Exception as  e:
        raise Http404()
    return render(request,'review.html',{"vote_form":vote_form,"single_project":single_project,"average_score":average_score})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = User.objects.filter(username=search_term)
        message = f"{search_term}"
        profiles=  Profile.objects.all()

        return render(request, 'search.html',{"message":message,"users": searched_users,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})    


