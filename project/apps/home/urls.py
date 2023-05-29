from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
]
