from django.urls import path

from . import views as account_views
from . import models as account_models
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'user', account_views.ProjectUserViewSet,
                 basename=account_models.ProjectUser)

router.register(r'patient', account_views.PatientViewSet,
                basename=account_models.Patient)
urlpatterns = [
    
    path('login/', account_views.UserLoginView.as_view())
]

urlpatterns += router.urls