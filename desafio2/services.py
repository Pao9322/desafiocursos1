from django.db import models

from .models import Estudiante, Profesor, Curso, CursoEstudiante, Direccion

def crear_estudiante(rut, nombre, apellido, fecha_nacimiento, creado_por=None):
    """
    Crea un nuevo estudiante en el sistema.

    Args:
        rut (str): RUT del estudiante.
        nombre (str): Nombre del estudiante.
        apellido (str): Apellido del estudiante.
        fecha_nacimiento (date): Fecha de nacimiento del estudiante.
        creado_por (str, opcional): Nombre de la persona que creó el estudiante.

    Returns:
        Estudiante: Objeto Estudiante creado.
    """
    estudiante = Estudiante.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nacimiento=fecha_nacimiento,
        creado_por=creado_por,
    )
    return estudiante



def crear_profesor(rut, nombre, apellido, activo, creado_por=None):
    """
    Crea un nuevo profesor en el sistema.

    Args:
        rut (str): RUT del profesor.
        nombre (str): Nombre del profesor.
        apellido (str): Apellido del profesor.
        activo (bool): Indica si el profesor está activo.
        creado_por (str, opcional): Nombre de la persona que creó el profesor.

    Returns:
        Profesor: Objeto Profesor creado.
    """
    profesor = Profesor.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        activo=activo,
        creado_por=creado_por,
    )
    return profesor



def crear_curso(codigo, nombre, version, profesor):
    """
    Crea un nuevo curso en el sistema.

    Args:
        codigo (str): Código del curso.
        nombre (str): Nombre del curso.
        version (int): Versión del curso.
        profesor (Profesor): Objeto Profesor que imparte el curso.

    Returns:
        Curso: Objeto Curso creado.
    """
    curso = Curso.objects.create(
        codigo=codigo,
        nombre=nombre,
        version=version,
        profesor=profesor,  
    )
    return curso




def crear_direccion(calle, numero, dpto, comuna, ciudad, region, profesor=None):
    """
    Crea una nueva dirección en el sistema.

    Args:
        calle (str): Nombre de la calle.
        numero (str): Número de la casa.
        dpto (str): Número de departamento (opcional).
        comuna (str): Nombre de la comuna.
        ciudad (str): Nombre de la ciudad.
        region (str): Nombre de la región.
        profesor (Profesor, opcional): Objeto Profesor asociado a la dirección.

    Returns:
        Direccion: Objeto Dirección creado.
    """
    direccion = Direccion.objects.create(
        calle=calle,
        numero=numero,
        dpto=dpto, 
        comuna=comuna,
        ciudad=ciudad,
        region=region,
    )

    if profesor:
        direccion.profesor = profesor
        direccion.save()

    return direccion






def obtiene_estudiante(rut):
    """
    Obtiene un estudiante por su RUT.

    Args:
        rut (str): RUT del estudiante.

    Returns:
        Estudiante: Objeto Estudiante o None si no se encuentra.
    """
    try:
        return Estudiante.objects.get(rut=rut)
    except Estudiante.DoesNotExist:
        return None




def obtiene_profesor(rut):
    """
    Obtiene un profesor por su RUT.

    Args:
        rut (str): RUT del profesor.

    Returns:
        Profesor: Objeto Profesor o None si no se encuentra.
    """
    try:
        return Profesor.objects.get(rut=rut)
    except Profesor.DoesNotExist:
        return None



def obtiene_curso(codigo):
    """
    Obtiene un curso por su código.

    Args:
        codigo (str): Código del curso.

    Returns:
        Curso: Objeto Curso o None si no se encuentra.
    """
    try:
        return Curso.objects.get(codigo=codigo)
    except Curso.DoesNotExist:
        return None
