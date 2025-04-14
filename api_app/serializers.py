from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artist
        fields = '__all__'

class MangasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manga
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password'
                  ]
        extra_kwargs = {
                'password': {'write_only': True}
                }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


