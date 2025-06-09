from django.shortcuts import render,redirect,get_object_or_404
from .models import Campaña, Donacion,ONG,Donante
from django.db.models import Sum
from .forms import ONGForm
from .forms import DonanteForm
from .forms import DonacionForm
from .forms import CampañaForm

from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.utils import timezone

def test(request):
    return render(request, 'core/test.html')

def home(request):
    return render(request, 'core/home.html')

def salir(request):
    logout(request)
    return redirect('inicio')

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request,usuario)
            return redirect('lista_publicaciones')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form':form})

@login_required
def inicio(request):
    campañas = Campaña.objects.all()
    return render(request, 'core/inicio.html', {'campañas': campañas})

@login_required
def crear_campaña(request):
    if request.method == 'POST':
        form = CampañaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CampañaForm()
    return render(request, 'core/crear_campaña.html', {'form': form})
#para el CRUD DE HISTORILA DE DONACIONES

@login_required
def crear_donacion(request):
    if request.method == 'POST':
        form = DonacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = DonacionForm()
    return render(request, 'core/crear_donacion.html', {'form': form})

def listar_donaciones(request):
    donaciones = Donacion.objects.all().order_by('-fecha')
    return render(request, 'core/historial_donaciones.html', {'donaciones': donaciones})

def editar_donacion(request, id):
    donacion = get_object_or_404(Donacion, id=id)
    if request.method == 'POST':
        form = DonacionForm(request.POST, instance=donacion)
        if form.is_valid():
            form.save()
            return redirect('historial_donaciones')
    else:
        form = DonacionForm(instance=donacion)
    return render(request, 'core/crear_donacion.html', {'form': form})

def eliminar_donacion(request, id):
    donacion = get_object_or_404(Donacion, id=id)

    if request.method == 'POST':
        donacion.delete()
        return redirect('historial_donaciones')  

    return render(request, 'core/confirmar_eliminacion.html', {'objeto': donacion})
#FIN DEL CRUD historial_donaciones

@login_required
def crear_ong(request):
    if request.method == 'POST':
        form = ONGForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ONGForm()
    return render(request, 'core/crear_ong.html', {'form': form})

@login_required
def crear_donante(request):
    if request.method == 'POST':
        form = DonanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = DonanteForm()
    return render(request, 'core/crear_donante.html', {'form': form})
