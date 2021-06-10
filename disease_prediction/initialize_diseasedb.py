from .models import Disease
import pickle
from .data_preprocess_util import del_duplicates_from_symptoms

def ini_db():
    if (Disease.objects.all().first() == None):
        disease_obj_file = open('disease_prediction/disease_obj_list','rb') 
        disease_obj_list = pickle.load(disease_obj_file)
        

        for i in disease_obj_list:
            symptom = del_duplicates_from_symptoms(i.selectionPool)
            symptom_to_add = " ,".join(symptom)
            to_add = Disease(name=i.name, symptoms=symptom_to_add)
            Disease.save(to_add)
    else :
        print("DB already exists !")