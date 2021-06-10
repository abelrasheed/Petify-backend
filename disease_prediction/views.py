from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pickle
from disease_prediction.prediction import prediction
from disease_prediction.data_preprocess_util import symp_process
from .models import Disease

# Create your views here.
sympfile = open('disease_prediction/symp_list_to_send','rb')
symp_list = pickle.load(sympfile)
diction ={
    "symptoms" : symp_list
}


@api_view(['GET'])
def symptoms_return(request):
        return Response(diction)


@api_view(['POST'])
def predict(request):
        symptoms = request.data['symptoms']
        trainable_symptoms = []
        for i in symptoms:
            temp = symp_process(i)
            trainable_symptoms.append(temp)
        disease = prediction(trainable_symptoms)
        predicted = {"prediction" : disease}
        return Response(predicted)

@api_view(['GET'])
def get_description(request,id_field):
        disease = Disease.objects.get(id=id_field)
        symptoms = disease.symptoms
        symptoms = symptoms.split(",")
        description = {
            "Name" : disease.name,
            "Symptoms" : symptoms,
            "Description" : disease.description
        }   
        return Response(description)