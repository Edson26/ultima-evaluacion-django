from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import FormInscritos, FormInstituto
from .models import Inscritos, Instituto

# Funcion para renderizar la pagina principal
def home(request):
    return render(request, 'index.html')

# Funcion para agregar una inscripcion
def agregar(request):
    form = FormInscritos()
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if (form.is_valid()):
            form.save()
        return home(request)
    data = {'form': form}
    return render(request, 'agregar.html', data)

# Funcion para listar los inscritos
def listadoInscritos(request):
    inscrito = Inscritos.objects.all()
    data = {'inscrito': inscrito}
    return render(request, 'listado.html', data)

# Funcion para editar una inscripcion
def editar(request, id):
    if request.method == 'GET':
        inscrito = Inscritos.objects.get(id=id)
        form = FormInscritos(instance=inscrito)
        data = {'form': form}
        return render(request, 'editar.html', data)
    else:
        try:
            inscrito = Inscritos.objects.get(id=id)
            form = FormInscritos(request.POST, instance=inscrito)
            if form.is_valid():
                form.save()
            return listadoInscritos(request)
        except ValueError:
            return render(request, 'editar.html', {'form': form, 'error': 'no fue posible actualizar inscripcion'})
       
# Funcion para eliminar una inscripcion
def eliminar(request, id):
    inscrito = Inscritos.objects.get(id=id)
    inscrito.delete()
    return listadoInscritos(request)