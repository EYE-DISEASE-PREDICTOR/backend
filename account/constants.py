from django.db import models


class Gender(models.TextChoices):
    M = 'male'
    F = 'female'

class MartialStatus(models.TextChoices):
    Y = 'married'
    N = 'not-married'
    D = 'divorced'