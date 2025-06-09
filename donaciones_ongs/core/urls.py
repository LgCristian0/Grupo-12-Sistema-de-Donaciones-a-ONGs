from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    
    path('campaña/', views.inicio, name='inicio'),  # Página de inicio
    path('crear-campaña/', views.crear_campaña, name='crear_campaña'),  
    # Esta es la página para crear una nueva campaña
    path('crear-donacion/', views.crear_donacion, name='crear_donacion'),
    path('editar-donacion/<int:id>/', views.editar_donacion, name='editar_donacion'),
    path('eliminar-donacion/<int:id>/', views.eliminar_donacion, name='eliminar_donacion'),
    path('historial-donaciones/', views.listar_donaciones, name='historial_donaciones'),
    path('crear-ong/', views.crear_ong, name='crear_ong'),
    path('crear-donante/', views.crear_donante, name='crear_donante'),

    path('logout/',views.salir,name='salir'),
    path('registro/', views.registrar, name='registrar'),

    path('test/', views.test, name='test'),
]