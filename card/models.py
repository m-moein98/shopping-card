from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=200)