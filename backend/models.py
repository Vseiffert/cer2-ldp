from django.db import models

# Create your models here.

class Number(models.Model):
    number = models.IntegerField()
    letter = models.CharField()

class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    pokedex_number = models.IntegerField()
    primary_type = models.CharField(max_length=15)
    secondary_type = models.CharField(max_length=15, null=True, blank=True)
    description = models.CharField(max_length=200, default= 'No existe descripcion para este pokemon')
    image_url = models.URLField(max_length=200, default='https://images.wikidexcdn.net/mwuploads/wikidex/4/4f/latest/20230130122413/Pok%C3%A9_Ball_HOME.png')

