from django.db import models

# Create your models here.
class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.rut} - {self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"


class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateTimeField(auto_now_add=True)
    modificacion_registro = models.DateTimeField(auto_now=True)
    creado_por = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.rut} - {self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"


class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, null=True, blank=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.calle}, {self.numero}, {self.ciudad}, {self.region}"

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"


class Curso(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    version = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, through='CursoEstudiante')

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class CursoEstudiante(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
