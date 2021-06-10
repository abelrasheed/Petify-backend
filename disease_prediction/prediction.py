import pickle
from collections import Counter
from disease_prediction.data_preprocess_util import dataArrange
# import disease_prediction.decision_tree_scratch as decision_tree_scratch 
from disease_prediction import decision_tree_scratch 
from .models import Disease


def prediction(X_raw):
    sympfile = open('disease_prediction/symp_model','rb') 
    symp_list = pickle.load(sympfile)

    # infile = open('disease_prediction/model','rb')
    # clf = pickle.load(infile)

    infile = open('disease_prediction/model','rb')
    clf = pickle.load(infile)

    encode_file = open('disease_prediction/encode_model','rb')
    encode = pickle.load(encode_file)

    X = dataArrange(symp_list , X_raw)
    X = [X]

    pred_array = []
    for count in range(10):
        pred = (clf[count].predict(X))
        pred = encode.inverse_transform(pred)
        pred_array.append(pred[0])
    

    counter = Counter(pred_array)
    iterator = counter.most_common()

    disease_prediction = []

    for i in iterator:
      
        probability = i[1]
        probability/=10
        probability *= 100
        disease = Disease.objects.get(name=i[0])
        temp = { "disease" : disease.name,"id" : disease.id, "probability" : probability}
        disease_prediction.append(temp)
    
    return disease_prediction

    infile.close
    sympfile.close
    encode_file.close

