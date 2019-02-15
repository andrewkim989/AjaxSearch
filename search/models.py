from django.db import models

class Creature(models.Model):
    name = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255)
    image = models.CharField(max_length = 255)
    species = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()