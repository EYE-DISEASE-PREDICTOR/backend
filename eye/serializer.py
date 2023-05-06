from rest_framework import serializers
from . import models as eye_models
from eye_predictor.settings import BASE_DIR



class EyeSerializer(serializers.ModelSerializer):
    class Meta:
        model = eye_models.Eye
        fields = '__all__'
        
    def to_representation(self, instance):
        print(BASE_DIR)

        return super().to_representation(instance)