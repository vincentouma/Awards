from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('',views.home,name = 'home'),
    url(r'^new_projects/$', views.new_projects, name='new_projects'),
    url(r'^projects/(\d+)',views.projects,name='projects'),
    url(r'profile',views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),


]