from django.db import models


class EyePosition(models.TextChoices):
    L = 'left'
    R = 'right'

class EyeCondition(models.IntegerChoices):
    NORMAL = 3
    GLAUCOMA = 2
    DIABETIC_RETINOPATHY = 1
    CATARACT = 0
    
