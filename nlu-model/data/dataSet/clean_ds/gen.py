from data import colors, inform_intents, intents, get_objects, sizes
import pprint
import re


objects = get_objects()
f = open('./toFill.md','r')
w = open('./nlu.md','w+')
for line in f.readlines():
    if line.startswith('-'):
        line = re.sub(r'\[\]\((.+?)\)',r'[\g<1>](\g<1>)',line)
        print(line)