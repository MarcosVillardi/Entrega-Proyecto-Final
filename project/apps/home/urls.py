from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('registrar_habitacion/', views.registrar_habitacion, name='registrar_habitacion'),
    path('registrar_garaje/', views.registrar_garaje, name='registrar_garaje'),
]
