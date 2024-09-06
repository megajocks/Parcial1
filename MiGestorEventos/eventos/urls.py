# eventos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.eventos_list, name='eventos_list'),
]
