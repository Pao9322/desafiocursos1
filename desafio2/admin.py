from django.contrib import admin
from .models import Estudiante, Profesor, Curso, CursoEstudiante, Direccion

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(CursoEstudiante)
admin.site.register(Direccion)