from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Evento
from .forms import EventoForm


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
            return redirect('lista_eventos')  # Redirige a la lista de eventos después de guardar
    else:
        form = EventoForm()
    
    return render(request, 'eventos/crear_evento.html', {'form': form})