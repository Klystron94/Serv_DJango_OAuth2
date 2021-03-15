from django.shortcuts import render

from rest_framework import viewsets
from appCompradores.models import Compradores
from appCompradores.serializers import CompradorSerializer
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
import requests

# class CompradorViewSet(viewsets.ModelViewSet):
#     model = Compradores
#     queryset = Compradores.objects.all()
#     serializer_class = CompradorSerializer


@api_view(['POST'])
@authentication_classes((SessionAuthentication, TokenAuthentication))
def crear(request):                                                    #Método para añadir compradores
    # try:
    #     comprador = Compradores.objects.get(pk=pk)
    # except Compradores.DoesNotExist:
    #     return HttpResponse(status=404)

    if request.method == 'POST':
        serializer = CompradorSerializer(data = request.data,many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((SessionAuthentication, TokenAuthentication))
def lista(request):                                                     #Método para mostrar listado de usuarios

    # try:
    #     comprador = Compradores.objects.get(pk=pk)
    # except Compradores.DoesNotExist:
    #     return HttpResponse(status=404)

    if request.method == 'GET':
        compradores = Compradores.objects.all()
        serializer = CompradorSerializer(compradores, many=True)
        return Response(serializer.data)
   

@api_view(['GET'])
@authentication_classes((SessionAuthentication, TokenAuthentication))
def usuario(request,id):                                                    #Método para mostrar un usuario
    if request.method == 'GET':
        try: 
            comprador = Compradores.objects.get(pk=id)
            serializer = CompradorSerializer(comprador) 
            print('este es el id' + str(comprador))
        except Compradores.DoesNotExist: 
            return JsonResponse({'mensaje': 'El comprador no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes((SessionAuthentication, TokenAuthentication))
def eliminar (request,id):                  #Método para borrar un usuario
    if request.method == 'DELETE':
        try: 
            comprador = Compradores.objects.filter(id=id).delete()

        except Compradores.DoesNotExist: 
            return JsonResponse({'mensaje': 'El comprador no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    return Response("El usuario fue eliminado!!")


@api_view(['GET'])
@authentication_classes((SessionAuthentication, TokenAuthentication))
def geo (request):                                                          #Método para geocodificar
    if request.method == 'GET':
        comprador = Compradores.objects.filter(estado_geo=False)
        vector = []
        for i in comprador:
            #print (i.direccion)
            direccion = i.direccion.replace('#','')
            direccion = direccion.replace('-',' ')
            direccion = direccion.replace(' ',',')
            print(direccion)
            res = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address={}+{}&key=AIzaSyDlmeg0VOQzbGnYDlYaRapYCG6w_DmnB54".format(direccion,i.ciudad))
            dic = res.json()
            lat = dic['results'][0]['geometry']['location']['lat']
            lng = dic['results'][0]['geometry']['location']['lng']
            Compradores.objects.filter(id=i.id).update(latitud=lat,longitud=lng,estado_geo=True)
            vector.append(i.id)
        #serializer = CompradorSerializer(comprador, many=True)
        return Response('Los usuarios '+str(vector)+' han sido actualizados')
        



@api_view(['GET'])
@authentication_classes((SessionAuthentication, TokenAuthentication))
def auth_test(request):                 #Test para probar autenticación admin
    return Response("it's great to have you here with token auth!!")

