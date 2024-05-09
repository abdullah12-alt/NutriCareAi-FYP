from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Ally_chat'),
    path('chat/', views.chat, name='chat_post'),  # Map '/chat' (POST) to the chat view for handling user input

    
]

