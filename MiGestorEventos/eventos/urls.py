from django.urls import path
from .views import OrganizadorListView, OrganizadorCreateView, EventoUpdateView, EventoCreateView, EventoUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('organizadores/', OrganizadorListView.as_view(), name='organizador_list'),
    path('organizadores/nuevo/', OrganizadorCreateView.as_view(), name='organizador_create'),
    path('eventos/', EventoListView.as_view(), name='evento_list'),
    path('eventos/nuevo/', EventoCreateView.as_view(), name='evento_create'),
    path('eventos/<int:pk>/editar/', EventoUpdateView.as_view(), name='evento_edit'),

]
