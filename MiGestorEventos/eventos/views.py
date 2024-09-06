# eventos/views.py
from django.shortcuts import render
from .models import Evento
# eventos/views.py
from django.shortcuts import render, redirect
from .forms import EventoForm


def eventos_list(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/eventos_list.html', {'eventos': eventos})


def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventos_list')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})


