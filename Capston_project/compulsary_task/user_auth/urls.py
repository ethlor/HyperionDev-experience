from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
         name='authenticate_user'),
    path('register_user/', views.register_user, name='register_user')
]