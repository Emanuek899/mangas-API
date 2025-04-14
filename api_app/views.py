from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
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


@api_view(['POST'])
def register_user(request):
    """
    API view to register users and generate a token for the user
    """
    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'data': serializer.data, 'Token': token.key})

    return Response(serializer.errors, status=400)


def new_manga(request):
    return render(request, 'api_app/new-manga.html')


