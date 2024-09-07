from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Evento, Organizador
from .forms import EventoForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

def index(request):
    return HttpResponse("Bienvenido a la gestión de eventos.")


def lista_eventos(request):
    eventos = Evento.objects.select_related('organizador').all()  
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})
    


def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos') 
    else:
        form = EventoForm()
    
    return render(request, 'eventos/crear_evento.html', {'form': form})
   


class OrganizadorListView(ListView):
    model = Organizador
    template_name = 'eventos/lista_organizadores.html'
    context_object_name = 'organizadores'  
    
class OrganizadorCreateView(CreateView):
    model = Organizador
    template_name = 'eventos/crear_organizador.html'
    fields = ['nombre', 'email']
    success_url = reverse_lazy('lista_organizadores') 