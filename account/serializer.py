from rest_framework import serializers
from django.contrib.auth import authenticate
from account import models as account_models



class LoginSerializer(serializers.Serializer):
    """Serializer for login"""

    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        try:
            user = account_models.ProjectUser.objects.get(username=validated_data['username'])
        except:
            raise AttributeError('username not found')

        validated_data['user'] = user.id
        
        return user

    def validate(self, attrs):
        """overriding to check password and username match"""
        username = attrs.get("username")
        password = attrs.get("password")
        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password
            )
            if not user:
                raise serializers.ValidationError(
                    "unable to authenticate with given credentials \
                    please check the given details",code="authorization")
            attrs['user'] = user
        else:
            raise AttributeError("Must include username and password")
        return attrs
    

class ProjectUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    class Meta:
            model = account_models.ProjectUser
            fields = '__all__'
        
    def update(self, instance, validated_data):
        """ overriden to check whether the instance is of request user"""
        
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            instance.save()

        return super().update(instance, validated_data)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.Patient
        fields = '__all__'