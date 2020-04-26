from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from api.serializers import CitySerializer, CategorySerializer, DoctorSerializer
from api.models import Category, City, Doctor

from django.http.response import JsonResponse

@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    return JsonResponse(CategorySerializer(categories, many=True).data, safe=False)

@api_view(['GET'])
def cities(request):
    categories = City.objects.all()
    return JsonResponse(CitySerializer(cities, many=True).data, safe=False)

class Doctors(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        return JsonResponse(DoctorSerializer(doctors, many=True).data, safe=False)

