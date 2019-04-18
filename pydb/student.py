
from django.db import models

class Stuent(models.Model):
    id = models.IntegerField()

    name = models.CharField(max_length=255)

    score = models.FloatField()


class Bole(models.Model):

    id = models.IntegerField()

    title = models.CharField(max_length=255)

    type = models.CharField(max_length=255)

    url = models.CharField(max_length=255)

    time = models.CharField(max_length=255)



