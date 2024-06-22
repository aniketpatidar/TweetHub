from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('create', views.create, name='tweet_create'),
    path('<int:id>/edit/', views.edit, name='tweet_edit'),
    path('<int:id>/delete/', views.delete, name='tweet_delete'),
    path('register', views.register, name='register'),
]