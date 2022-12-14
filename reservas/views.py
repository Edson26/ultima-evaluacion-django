from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import FormInscritos, FormInstituto
from .models import Inscritos, Instituto

# Funcion para renderizar la pagina principal


def home(request):
    return render(request, 'index.html')

# Funcion para agregar una inscripcion


def crearInscripcion(request):
    form = FormInscritos()
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if (form.is_valid()):
            form.save()
        return listadoInscrito(request)
    data = {'form': form}
    return render(request, 'crear_inscripcion.html', data)

# Funcion para agregar Instituto


def crearInstituto(request):
    form = FormInstituto()
    if request.method == 'POST':
        form = FormInstituto(request.POST)
        if (form.is_valid()):
            form.save()
        return home(request)
    data = {'form': form}
    return render(request, 'crear_instituto.html', data)

# Funcion para listar los inscritos


def listadoInscrito(request):
    inscrito = Inscritos.objects.all()
    data = {'inscritos': inscrito}
    return render(request, 'listar_inscripcion.html', data)

# Funcion para listar los institutos


def listadoInstituto(request):
    instituto = Instituto.objects.all()
    data = {'instituto': instituto}
    return render(request, 'listar_instituto.html', data)

# Funcion para editar una inscripcion


def editarInscrito(request, id):
    if request.method == 'GET':
        inscrito = Inscritos.objects.get(id=id)
        form = FormInscritos(instance=inscrito)
        data = {'form': form}
        return render(request, 'editar_inscripcion.html', data)
    else:
        try:
            inscrito = Inscritos.objects.get(id=id)
            form = FormInscritos(request.POST, instance=inscrito)
            if form.is_valid():
                form.save()
            return listadoInscrito(request)
        except ValueError:
            return render(request, 'editar_inscripcion.html', {'form': form, 'error': 'no fue posible actualizar la inscripcion'})

# Funcion para editar un Instituto


def editarInstituto(request, id):
    if request.method == 'GET':
        inscrito = Instituto.objects.get(id=id)
        form = FormInstituto(instance=inscrito)
        data = {'form': form}
        return render(request, 'editar_instituto.html', data)
    else:
        try:
            inscrito = Instituto.objects.get(id=id)
            form = FormInstituto(request.POST, instance=inscrito)
            if form.is_valid():
                form.save()
            return listadoInscrito(request)
        except ValueError:
            return render(request, 'editar_instituto.html', {'form': form, 'error': 'no fue posible actualizar la inscripcion'})


# Funcion para eliminar una inscripcion


def eliminar(request, id):
    inscrito = Inscritos.objects.get(id=id)
    inscrito.delete()
    return listadoInscrito(request)

# Funcion para eliminar un Instituto


def eliminar(request, id):
    inscrito = Instituto.objects.get(id=id)
    inscrito.delete()
    return listadoInstituto(request)
