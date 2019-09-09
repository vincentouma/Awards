from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name = 'home'),
    url(r'^new_projects/$', views.new_projects, name='new_projects'),
    url(r'^projects/(\d+)',views.projects,name='projects'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^edit/profile/$',views.profile_edit,name = 'edit_profile'),    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^accounts/profile/', views.profile, name="myProfile"),        



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
