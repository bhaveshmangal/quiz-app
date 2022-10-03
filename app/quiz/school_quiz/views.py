from django.shortcuts import render
from rest_framework import viewsets
from .models import StudentClass
from .serializers import StudentClassSerializer

class StudentClassViewSet(viewsets.ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer