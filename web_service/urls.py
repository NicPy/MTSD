from django.urls import path
from django.conf.urls import url
from web_service import views
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    url(r'^news/(?P<pk>\d+)/$', views.single_news, name='single_news'),
    path('charity/', views.charity, name='charity'), 
    path('profile/', views.profile, name='profile'), 
    url(r'^signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    url(r'^login/$', auth_views.login,{'template_name':'login.html'}, name='login'),

]