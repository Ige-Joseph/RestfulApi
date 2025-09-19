from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Books
from .serializers import Books_Serializers

class BookViewset(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = Books_Serializers