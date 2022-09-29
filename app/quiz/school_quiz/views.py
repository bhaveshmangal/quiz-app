from django.shortcuts import render
from rest_framework import viewsets
from .models import StudentClass, User, QuizScore
from .serializers import StudentClassSerializer, QuizScoreSerializer, UserSerializer

class StudentClassViewSet(viewsets.ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer


class QuizScoreViewSet(viewsets.ModelViewSet):
    queryset = QuizScore.objects.all()
    serializer_class = QuizScoreSerializer