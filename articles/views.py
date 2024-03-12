from django.shortcuts import render
from rest_framework import viewsets
from .models import Articlesdata
from .serializers import ArticlesSerializer

# Create your views here.
class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articlesdata.objects.all()
    serializer_class = ArticlesSerializer