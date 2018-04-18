from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    url(r'^news/(?P<pk>\d+)/$', views.single_news, name='single_news'),

]