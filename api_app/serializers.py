from rest_framework import serializers
from . import models

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artist
        fields = '__all__'

class MangasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manga
        fields = '__all__'
