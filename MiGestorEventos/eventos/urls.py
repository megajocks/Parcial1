from django.urls import path
from . import views
from .views import OrganizadorListView, OrganizadorCreateView



urlpatterns = [
   
    path('', views.lista_eventos, name='lista_eventos'),
     path('crear/', views.crear_evento, name='crear_evento'),
     path('organizadores/', OrganizadorListView.as_view(), name='lista_organizadores'),
    path('organizadores/crear/', OrganizadorCreateView.as_view(), name='crear_organizador'),
]