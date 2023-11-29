from django.shortcuts import render

# Create your views here.
# views.py

from rest_framework import generics
from .models import SeuModelo
from .serializers import SeuModeloSerializer

class SeuModeloListCreateView(generics.ListCreateAPIView):
    queryset = SeuModelo.objects.all()
    serializer_class = SeuModeloSerializer
