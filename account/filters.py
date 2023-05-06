import django_filters as filters
from .models import Patient

class PatientFilterSet(filters.FilterSet):
    user = filters.CharFilter(field_name='examiner')

    class Meta:
        model = Patient
        fields = ['user', ]
