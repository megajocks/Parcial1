# eventos/urls.py
from django.urls import path
from . import views
from django.urls import path
from .views import OrganizadorListView, OrganizadorCreateView

urlpatterns = [
    path('eventos/', views.eventos_list, name='eventos_list'),
]

urlpatterns += [
    path('organizadores/', OrganizadorListView.as_view(), name='organizador_list'),
    path('crear-organizador/', OrganizadorCreateView.as_view(), name='crear_organizador'),
]