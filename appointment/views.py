from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import parchi
from .serializers import parchiserializer

@api_view(['GET'])
def parchi_list(request):
    # Retrieve data from MyModel and serialize it
    data = parchi.objects.all()
    serializer = parchiserializer( data , many=True)
    return Response(serializer.data)

@api_view(['POST'])
def parchi_create(request):
    # Deserialize the request data and save it to MyModel
    serializer = parchiserializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)