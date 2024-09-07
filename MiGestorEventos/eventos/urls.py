from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define una ruta para la vista index
]
