import random

colors = {'red':'#FF0000',
          'green':'#009900',
          'blue':'#0000FF',
          'black':'#FFFFFF',
          'white':'#0000FF'}

sizes = ['small', 'medium', 'large']

intents = ['print a', 'print a', 'make a', 'create a', 
           'i want a', 'give me a', 'produce a', 'i need a',
           'i would like a' ]

inform_intents = ['it\'s a',
                  'it\'s', 
                  'it is a', 
                  'it is', 
                  'let it be a', 
                  'let it be',
                  'make it a',
                  'try with a',
                  'try with',
                  'make it']

def get_objects(ration=0.2):
    uncleaned = []
    objects = []
    with open('nlu-model/data/generate_ds/data.single', 'r') as f:
        uncleaned = f.readlines()
        for o in uncleaned:
           objects.append(o.rstrip().lower())
    return random.sample(objects, int(len(objects)*ration))
