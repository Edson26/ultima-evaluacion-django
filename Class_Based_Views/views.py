from django.shortcuts import render
from Class_Based_Views.serializers import InscritosSerializer
from seminario.models import Inscritos
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class ListaInscritos(APIView):
    def get(self, request):
        insc = Inscritos.objects.all()
        serial = InscritosSerializer(insc, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleInscritos(APIView):
    def get_object(self, pk):
        try:
            return Inscritos.objects.get(id=pk)
        except Inscritos.DoesNotExist:
            return Http404

    def get(self, request, pk):
        insc = self.get_object(pk)
        serial = InscritosSerializer(insc)
        return Response(serial.data)

    def put(self, request, pk):
        insc = self.get_object(pk)
        serial = InscritosSerializer(insc, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        insc = self.get_object(pk)
        insc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)