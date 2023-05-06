from django.urls import path

from . import views as eye_views
from . import models as eye_models
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'', eye_views.EyeViewSet,
                 basename=eye_models.Eye)

urlpatterns = [
    path('disease/check/', eye_views.EyeCheckView.as_view(), name='check')
   
]

urlpatterns += router.urls