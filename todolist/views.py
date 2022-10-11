from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
