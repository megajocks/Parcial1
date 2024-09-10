from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Organizador
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from .models import Evento
from .forms import EventoForm

class OrganizadorListView(ListView):
    model = Organizador
    template_name = 'organizador_list.html'
    context_object_name = 'organizadores'


class OrganizadorCreateView(CreateView):
    model = Organizador
    fields = ['nombre', 'email']
    template_name = 'organizador_form.html'
    success_url = reverse_lazy('organizador_list')

class EventoListView(ListView):
    model = Evento
    template_name = 'evento_list.html'
    context_object_name = 'eventos'

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento_form.html'
    success_url = reverse_lazy('evento_list')
    
@method_decorator(login_required, name='dispatch')
class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento_form.html'
    success_url = reverse_lazy('evento_list')