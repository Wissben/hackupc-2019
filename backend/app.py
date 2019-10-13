from flask import Flask, render_template, request
from rasa_nlu.model import Metadata, Interpreter
from settings import PATHS
from rasa_nlu.model import Interpreter
import requests
from flask import jsonify
from flask_cors import CORS
import os
from words_similarity import get_synonyms
import random


interpreter = Interpreter.load(PATHS['model'])
state = {'color':False,'object':False,'size':False}
repetition_counter = 0

app = Flask(__name__)
CORS(app)

def parse(request):
    semantic_frame = interpreter.parse(request)
    intent = semantic_frame['intent']['name']
    entities = [{'entity':ent['entity'],'value':ent['value']} for ent in semantic_frame['entities']]
    text = semantic_frame['text']
    return intent,entities,text

def transform_to_action(intent,entities,text):
    color, size, name = get_printing_specifications(entities)
    action = ''
    if intent is 'unknown':
        action = {
                    'intent':'inform',
                    'entities' : [],
                    'text' : 'I did not understand you'
        }

    if color is None:
        action = {
                    'intent':'ask',
                    'entities' : ['color'],
                    'text' : 'What is the color of the object ?'
        }
    if size is None:
         action = {
                    'intent':'ask',
                    'entities' : ['size'],
                    'text' : 'What is the size of the object ?'
        }    
    if name is None:
        action = {
                    'intent':'ask',
                    'entities' : ['name'],
                    'text' : 'What is the action of the object ?'
        }
        
    match = find_corresponding_model(name)
    if match is not None:
        model_path = "object_models/"+match+".obj"
        return action, model_path, color, size
    else:
        return None

def get_directory_files(path):
    cleaned_files = []
    for root, dirs, files in os.walk(path):
        None
    for f in files:
        cleaned_files.append(f.split(".obj")[0])
    return cleaned_files



def check_color(entity):
    if entity['entity'] == "color":
        return entity['value']
    return None


def check_size(entity):
    if entity['entity'] == "size":
        return entity['value']
    return None


def check_object_name(entity):
    if entity['entity'] == "object":
        return entity['value']
    return None


def get_printing_specifications(entities):
    color, found_c = None, False
    size, found_s = None, False
    name, found_n = None, False
    for entity in entities:
        if not found_c:
            color = check_color(entity)
            if color is not None:
                found_c = True

        if not found_s:
            size = check_size(entity)
            if size is not None:
                found_s = True

        if not found_n:
            name = check_object_name(entity)
            if name is not None:
                found_n = True

        if found_c and found_n and found_s:
            return color, size, name

    return color, size, name


def find_corresponding_model(object_name):
    available_models = get_directory_files("./object_models/")
    if object_name in available_models:
        return object_name
    else:
        synonyms = get_synonyms(object_name)
        for synonym in synonyms:
            if synonym in available_models:
                return synonym

    return None



@app.route("/api/req", methods=['GET'])
def get_bot_response():
    global state 
    global repetition_counter
    intent,entities,text = parse(str(request.args.get('text')))
    model = None
    ret = 'B I E N E'
    print(intent)
    print(entities)
    print(text)

    if intent == 'inform' or 'print':
        print('heeeeeeeeeeeeeeeeee {}'.format(entities))
        for ent in entities :
            state[ent['entity']]=ent['value']
        if all(state.values()):
            model = find_corresponding_model(state['object'])
            if model == None :
                ret = 'I did not find your 3D model',None
            else :
                ret = 'I found your model, it is a {} and is displayed just beneath'.format(model),model
        else:
            for s in state :
                if not state[s] :
                    ret = 'Please, can you give me the {} ?'.format(s)
                    repetition_counter +=1
                    if repetition_counter > 5 and not state[s] :
                        break
            
    else :
        if intent == 'cancel' :
            state = {'color':False,'object':False,'size':False}
            model = None
            ret = 'Okay, I have cancelled the request'
        else :
            if intent == 'confirm' or intent == 'deny' :
                ret = 'Okay cool bruh'
            else :
                if intent == 'unknown':
                    ret = 'B I E N E BUT BETTER'
    print(model)
    return jsonify(
        text=ret,
        model=model
    )



if __name__ == '__main__':
    app.run()

