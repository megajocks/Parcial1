from django.urls import path
from .views import OrganizadorListView, OrganizadorCreateView, EventoUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('organizadores/', OrganizadorListView.as_view(), name='organizador_list'),
    path('organizadores/nuevo/', OrganizadorCreateView.as_view(), name='organizador_create'),
    path('eventos/<int:pk>/editar/', EventoUpdateView.as_view(), name='evento_edit'),
    path('eventos/nuevo/', EventoCreateView.as_view(), name='evento_create'),
    path('eventos/<int:pk>/editar/', EventoUpdateView.as_view(), name='evento_edit'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
