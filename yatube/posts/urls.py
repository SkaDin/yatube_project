from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:_fil_post>/', views.group_posts),
] 
