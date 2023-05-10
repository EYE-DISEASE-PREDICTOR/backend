from django.shortcuts import render
from rest_framework import viewsets, generics, views
from . import serializer as eye_serializer
from . import models as eye_models
from account import models  as account_models 
from rest_framework.response import Response
from eye import constants as eye_constants
from tensorflow import keras
import cv2
import numpy as np
from eye_predictor.settings import BASE_DIR
import os
# Create your views here.

class EyeViewSet(viewsets.ModelViewSet):
    serializer_class = eye_serializer.EyeSerializer
    queryset = eye_models.Eye.objects.all()


class EyeCheckView(views.APIView):
    def post(self, request):
        patient = request.data.get('patient', None)
        if not patient:
            return Response({"message":"enter patient id"})
        try:
            patient = account_models.Patient.objects.get(id=patient)
            eye = patient.eyes.all().last()
            image_path = str(eye.image)
        except:
            return Response({"message":"enter eye id"})
        
        file_path = os.path.join(BASE_DIR, 'h5/efficientnetb3-Eye Disease-93.84.h5')
        Model = keras.models.load_model(file_path)
        x=cv2.imread(image_path)
        x = cv2.resize(x,(224,224))     # resize image to match model's expected sizing
        x= x.reshape(1,224,224,3)
        preds = Model.predict(x)
        y_pred = np.argmax(preds, axis=1)
        eye.condition = y_pred
        data = {"result":eye_constants.EyeCondition(y_pred).label}
        eye.save()
        return Response(data)