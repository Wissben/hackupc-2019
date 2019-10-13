import json
PATH = 'train_intents.json'
OUT = 'unk.out'
out = open(OUT,'w+')
with open(PATH) as f:
    data = json.load(f)
    for k in data['train_dataset']['unknown']:
        out.write('- '+k['text'].lower()+'\n')

out.close()