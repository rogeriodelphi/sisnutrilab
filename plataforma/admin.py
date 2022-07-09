from django.contrib import admin
from .models import Paciente, DadosPaciente

admin.site.register(Paciente)
admin.site.register(DadosPaciente)

