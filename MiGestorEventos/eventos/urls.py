from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
]