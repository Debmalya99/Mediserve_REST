from flask import Flask,url_for,redirect,render_template,request,jsonify
import pickle
from utility import *
import json

######################################  LOAD RESOURCES  #########################################
print('[STATUS] Loading data')
data = pickle.load(open('resources/Mediserve-ML-data.pickle','rb'))
print('[STATUS] Loading models')
models = pickle.load(open('resources/Mediserve-ML-models.pickle','rb'))
print('[STATUS] Loading encoders')
encoders = pickle.load(open('resources/Mediserve-ML-encoders.pickle','rb'))
print('[STATUS] Loading severity data')
sevr_dict = pickle.load(open('resources/Mediserve-ML-severity-dict.pickle','rb'))
######################################  LOAD RESOURCES  #########################################

final_model = models[2][1] # DTREE

app = Flask(__name__)

@app.route('/api/mediserve/v1/<symptom>',methods=['GET'])
def process_symptom(symptom):
    symptom_dict = json.loads(symptom)
    symp_list = symptom_dict['symptoms']
    enc_symp = encode_data(symp_list,encoders)
    result = final_model.predict(enc_symp)
    result_text = decode_output(result,encoders)
    desc = get_description(result_text,data[3])
    precautions = get_precautions(result_text,data[4])
    severity = get_severity(sevr_dict,symp_list)
    return jsonify({"result":result_text,"description":desc,"precautions":precautions,"severity":severity})

if __name__ == "__main__":
    app.run()