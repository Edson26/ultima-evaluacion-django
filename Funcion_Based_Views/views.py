from django.shortcuts import render
from Funcion_Based_Views.serializers import InstitucionSerializer
from seminario.models import Institucion
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def listar_institucion(request):
    if request.method == 'GET':
        ins = Institucion.objects.all()
        serial = InstitucionSerializer(ins, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid() :
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_institucion(request, pk):
    try:
        ins = Institucion.objects.get(pk=pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = InstitucionSerializer(ins)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = InstitucionSerializer(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)