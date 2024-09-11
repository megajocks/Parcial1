from django.urls import path
from . import views
from .views import OrganizadorListView, OrganizadorCreateView, EventoListView, EventoCreateView, EventoUpdateView
from django.contrib.auth import views as auth_views
from .views import SignUpView 


urlpatterns = [
    path('organizadores/', views.OrganizadorListView.as_view(), name='organizadores_list'),
    path('organizadores/crear/', views.OrganizadorCreateView.as_view(), name='organizadores_create'),
    path('eventos/', views.EventoListView.as_view(), name='eventos_list'),
    path('eventos/crear/', views.EventoCreateView.as_view(), name='eventos_create'),
    path('eventos/<int:pk>/editar/', views.EventoUpdateView.as_view(), name='eventos_edit'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'), 
]
