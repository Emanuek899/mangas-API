from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.

class MangaViewSet(viewsets.ModelViewSet):
    queryset = models.Manga.objects.all()
    serializer_class = serializers.MangasSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer
