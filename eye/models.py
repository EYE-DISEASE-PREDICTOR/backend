from django.db import models
from  eye import constants as eye_constants
# Create your models here.
class Eye(models.Model):
    image = models.ImageField(upload_to="image/%y", 
                              null=True, default=True,
                              blank=True, max_length=500)
    position = models.CharField(
        default=eye_constants.EyePosition.L,
        choices=eye_constants.EyePosition.choices,max_length=10
    )
    patient = models.ForeignKey('account.Patient', 
                                on_delete=models.CASCADE,
                                blank=True, 
                                null=True, 
                                default='', 
                                related_name='eyes')
    condition = models.IntegerField(
        default=eye_constants.EyeCondition.NORMAL,
        choices=eye_constants.EyeCondition.choices,)