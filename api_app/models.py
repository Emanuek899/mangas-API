from django.db import models

# Create your models here.# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Artist(models.Model):
    name = models.CharField(max_length=200)
    last_name1 = models.CharField(max_length=100)
    last_name2 = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField()
    decease_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist'


class Manga(models.Model):
    name = models.CharField(max_length=200)
    volume = models.IntegerField()
    chapters = models.IntegerField()
    editorial = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, models.DO_NOTHING)
    creation_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'manga'
