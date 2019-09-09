from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from tinymce.models import HTMLField
from .forms import  *
from .models import *
# Create your views here.

def home(request):
   current_user = request.user
   projects = Projects
   return render(request,'home.html',{'projects':projects})
    
@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
            return render(request, 'profile.html')
    else:
        form = ProjectsForm()

        my_profile = Profile.objects.all()
    return render(request,'profile.html', locals())    

@login_required(login_url='/accounts/login/')
def new_projects(request):
    current_user = request.user
    profile = Profile.objects.get(user_id =current_user)
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

@login_required(login_url='/accounts/login/')
def projects(request,id):    
    post=Project.objects.get(id=id)
    votes = Votes.objects.filter(post=post)
    form = Votess()
    # Empty list for each of the category of votes
    design = []
    usability = []
    creativity = []
    content = []

    # For loop to appent the votes to the empty list
    for vote in votes:
                design.append(vote.design)
                usability.append(vote.usability)
                creativity.append(vote.creativity)
                content.append(vote.content)

    design = []
    usability = []
    creativity = []
    Content = []

    if len(usability)>0:
            usability = (sum(usability)//len(usability))
            usability.append(usability)
    if len(creativity)>0:
            creativity = (sum(creativity)//len(creativity))
            creativity.append(creativity)
    if len(design)>0:
            design = (sum(design)//len(design))
            design.append(design)
    if len(content)>0:
            content = (sum(content)//len(content))
            content.append(content)
    
    if request.method == 'POST':
            vote = Votess(request.POST)
            if vote.is_valid():
                    design = vote.cleaned_data['design']
                    usability = vote.cleaned_data['usability']
                    content = vote.cleaned_data['content']
                    creativity = vote.cleaned_data['creativity']
                    rating = Votes(design=design,usability=usability,
                                    content=content,creativity=creativity,
                                    user=request.user,post=post)
                    rating.save()
                    return redirect('home')
    return render(request,'projects.html',{"form":form, "design":design, "creativity":creativity, "content":content, "design":design, "usability":usability, "post":post})



@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = User.objects.filter(username=search_term)
        message = f"{search_term}"
        profiles=  Profile.objects.all( )

        return render(request, 'search.html',{"message":message,"users": searched_users,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})    


