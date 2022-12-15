from django.shortcuts import render
from .forms import FormInscritos, FormInstitucion
from .models import Inscritos, Institucion

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


def crearInstitucion(request):
    form = FormInstitucion()
    if request.method == 'POST':
        form = FormInstitucion(request.POST)
        if (form.is_valid()):
            form.save()
        return listadoInstitucion(request)
    data = {'form': form}
    return render(request, 'crear_institucion.html', data)

# Funcion para listar los inscritos


def listadoInscrito(request):
    inscrito = Inscritos.objects.all()
    data = {'inscritos': inscrito}
    return render(request, 'listar_inscripcion.html', data)

# Funcion para listar los institutos


def listadoInstitucion(request):
    institucion = Institucion.objects.all()
    data = {'instituciones': institucion}
    return render(request, 'listar_institucion.html', data)

# Funcion para editar una inscripcion


def editarInscrito(request, id):
    if request.method == 'GET':
        inscrito = Inscritos.objects.get(id=id)
        form = FormInscritos(instance=inscrito)
        return render(request, 'editar_inscripcion.html', {'inscrito': inscrito, 'form': form})
    else:
        try:
            inscrito = Inscritos.objects.get(id=id)
            form = FormInscritos(request.POST, instance=inscrito)
            if form.is_valid():
                form.save()
            return listadoInscrito(request)
        except ValueError:
            return render(request, 'editar_inscripcion.html', {'form': form, 'error': 'no fue posible actualizar la inscripción'})

# Funcion para editar un Instituto


def editarInstitucion(request, id):
    if request.method == 'GET':
        institucion = Institucion.objects.get(id=id)
        form = FormInstitucion(instance=institucion)
        data = {'form': form}
        return render(request, 'editar_institucion.html', data)
    else:
        try:
            institucion = Institucion.objects.get(id=id)
            form = FormInstitucion(request.POST, instance=institucion)
            if form.is_valid():
                form.save()
            return listadoInstitucion(request)
        except ValueError:
            return render(request, 'editar_institucion.html', {'form': form, 'error': 'no fue posible actualizar la institución'})


# Funcion para eliminar una inscripcion


def eliminarInscripcion(request, id):
    inscrito = Inscritos.objects.get(id=id)
    inscrito.delete()
    return listadoInscrito(request)

# Funcion para eliminar un Instituto


def eliminarInstitucion(request, id):
    institucion = Institucion.objects.get(id=id)
    institucion.delete()
    return listadoInstitucion(request)
