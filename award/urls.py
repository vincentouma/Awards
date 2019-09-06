from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('',views.home,name = 'home'),
    url(r'^new_projects/$', views.new_projects, name='new_projects'),

]