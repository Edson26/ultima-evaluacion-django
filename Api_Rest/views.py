from django.shortcuts import render
from django.http import JsonResponse
from seminario.models import Inscritos
# Create your views here.

def verinscritos(request):
    inscritos = Inscritos.objects.all()
    data = {'inscrito': list(inscritos.values('nombre','telefono','fecha','hora','institucion','estado','observacion'))}
    return JsonResponse(data)