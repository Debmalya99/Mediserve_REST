import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def encode_data(symptom_input,encoder_list):
    # symptom_input is a list
    # returns an np.ndarray
    i = 0
    symptom_array = list()
    for col_name,enc in encoder_list[1:][:]:
        symptom_array.append(int(enc.transform([symptom_input[i]])))
        i += 1
    return np.array(symptom_array).reshape(1,-1)

def decode_output(result,encoder_list):
    return encoder_list[0][1].inverse_transform(result)[0]


def get_description(res,desc_dataset):
    for index,row in desc_dataset.iterrows():
        if(row['Disease'] == res):
            return row['Description']

def get_precautions(res,prec_dataset):
    out_data = list()
    for index,row in prec_dataset.iterrows():
        if(row['Disease'] == res):
            for i in range(1,5):
                if(row['Precaution_'+str(i)] != 'not_needed'):
                    out_data.append(row['Precaution_'+str(i)])
    return out_data

def get_severity(sevr_dict,sym_list):
    sev = 0
    for m in sym_list:
        sev += sevr_dict[m]
    if sev in range(0,25):
        return 'Low'
    elif sev in range(25,50):
        return 'Medium'
    elif sev in range(50,75):
        return 'High'
    else:
        return 'Very High'
