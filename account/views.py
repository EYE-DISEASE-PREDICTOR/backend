from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework  import generics, viewsets
from . import serializer as account_serializer
from . import models as account_models
from . filters import PatientFilterSet

# Create your views here.
class UserLoginView(generics.CreateAPIView):
    """login for projectuser"""
    serializer_class = account_serializer.LoginSerializer

class ProjectUserViewSet(viewsets.ModelViewSet):
    serializer_class = account_serializer.ProjectUserSerializer
    queryset = account_models.ProjectUser.objects.all()


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = account_serializer.PatientSerializer
    queryset = account_models.Patient.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = PatientFilterSet