from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:filter_posts>/', views.group_posts),
] 
