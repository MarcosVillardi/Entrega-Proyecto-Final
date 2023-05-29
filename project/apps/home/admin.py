from django.contrib import admin
from . import models
admin.site.register(models.Cliente)
admin.site.register(models.Reserva)
admin.site.register(models.Garaje)