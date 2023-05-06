from django.contrib import admin
from account import models as account_models

# Register your models here.
admin.site.register(account_models.ProjectUser)
admin.site.register(account_models.Patient)