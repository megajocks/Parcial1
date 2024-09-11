from django.views.generic import ListView, CreateView, UpdateView
from .models import Organizador, Evento
from .forms import EventoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView




class OrganizadorListView(ListView):
    model = Organizador
    template_name = 'eventos/organizador_list.html'

class OrganizadorCreateView(CreateView):
    model = Organizador
    fields = ['nombre']
    template_name = 'eventos/organizador_form.html'
    success_url = '/organizadores/'

class EventoListView(ListView):
    model = Evento
    template_name = 'eventos/evento_list.html'
    context_object_name = 'eventos'

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/evento_form.html'
    success_url = reverse_lazy('eventos_list') 

class EventoUpdateView(LoginRequiredMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/evento_form.html'
    success_url = '/eventos/'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
        
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
def home(request):
    return render(request, 'home.html')
    
class HomeView(TemplateView):
    template_name = 'home.html'
    
class MenuView(TemplateView):
    template_name = 'menu.html'
    
def menu(request):
    return render(request, 'menu.html')