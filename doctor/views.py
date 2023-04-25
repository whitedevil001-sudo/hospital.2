from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import doctor
from .serializers import doctorserializer

@api_view(['GET'])
def doctor_list(request):
    # Retrieve data from MyModel and serialize it
    data = doctor.objects.all()
    serializer = doctorserializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def doctor_create(request):
    # Deserialize the request data and save it to MyModel
    serializer = doctorserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)