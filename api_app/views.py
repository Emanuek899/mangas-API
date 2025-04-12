from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.

class MangaViewSet(viewsets.ModelViewSet):
    """
    This viewset allows to manage all the petitions http
    (GET, POST, PUT, DELETE) in one

    """
    queryset = models.Manga.objects.all()
    serializer_class = serializers.MangasSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    """
    This viewset allows to manage all the petitions http
    (GET, POST, PUT, DELETE) in one

    """
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer

def new_manga(request):
    return render(request, 'api_app/new-manga.html')
