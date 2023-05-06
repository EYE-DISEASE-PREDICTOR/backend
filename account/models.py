from django.db import models
from django.contrib.auth.models import AbstractUser
from . import constants as account_constants

# Create your models here.
class ProjectUser(AbstractUser):
    phone = models.CharField(max_length=50, default='', blank=True, null=True)


    def save(self, *args, **kwargs):
        """
        hashes the password when account is created
        """
        
        if self.pk is None and self.is_superuser==False:
            self.set_password(self.password)
        super().save(*args, **kwargs)


class Patient(models.Model):
    first_name = models.CharField(
        max_length=100)
    last_name = models.CharField(
        max_length=100, default='', blank=True, null=True)
    gender = models.CharField(
        max_length=50, default=account_constants.Gender.F,
        choices=account_constants.Gender.choices,
        blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    birth_city = models.CharField(
        max_length=500, default='', blank=True, null=True)
    marital_status = models.CharField(
        max_length=50, default=account_constants.MartialStatus.N,
        choices=account_constants.MartialStatus.choices, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, default='', blank=True, null=True)
    age = models.PositiveIntegerField(default=None, blank=True, null=True)
    examiner = models.ForeignKey(
        'account.ProjectUser', default=None, blank=True, null=True, on_delete=
         models.CASCADE, related_name='patients')

