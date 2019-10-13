from data import colors, inform_intents, intents, get_objects, sizes
import pprint
import random

def get_types_of_sentences():
    sentences =dict()
    for i in range(1,12):
        sentences[i] = []
    return sentences


def generate_dataset():
    objects = get_objects()
    prints = get_types_of_sentences()
    informs = get_types_of_sentences()

    for intent in intents:
        for color in colors:
            for size in sizes:
                for object in objects:
                    prints[1].append(intent + " ["+color+"](color) ["+object+"](object)")
                    prints[2].append(intent + " ["+size+"](size) ["+object+"](object)")
                    prints[3].append(intent + " [" + size + "](size) ["+color+"](color) [" + object + "](object)")
                    prints[4].append(intent + " [" + color + "](color) thing")
                    prints[5].append(intent + " [" + color + "](color) painted [" + object + "](object)")
                    prints[6].append(intent + " [" + size + "](size) [" + color + "](color) painted [" + object + "](object)")
                    prints[7].append(intent + " [" + size + "](size) sized [" + color + "](color)+[" + object + "](object)")
                    prints[8].append(intent + " [" + color + "](color) colored [" + object + "](object)")
                    prints[9].append(intent + " [" + size + "](size) [" + color + "](color) colored [" + object + "](object)")
                    prints[10].append(intent + " [" + color + "](color) painted thing")

    for intent in inform_intents:
        for color in colors:
            for size in sizes:
                for object in objects:
                    informs[1].append(intent + " ["+color+"](color) ["+object+"](object)")
                    informs[2].append(intent + " ["+size+"](size) ["+object+"](object)")
                    informs[3].append(intent + " [" + size + "](size) ["+color+"](color) [" + object + "](object)")
                    informs[4].append(intent + " [" + color + "](color) thing")
                    informs[5].append(intent + " [" + color + "](color) painted [" + object + "](object)")
                    informs[6].append(intent + " [" + size + "](size) [" + color + "](color) painted [" + object + "](object)")
                    informs[7].append(intent + " [" + size + "](size) sized [" + color + "](color)+[" + object + "](object)")
                    informs[8].append(intent + " [" + color + "](color) colored [" + object + "](object)")
                    informs[9].append(intent + " [" + size + "](size) [" + color + "](color) colored [" + object + "](object)")
                    informs[10].append(intent + " [" + color + "](color) painted thing")


    return prints, informs


def generate_md_file():
    with open('nlu-model/data/nlu.md', 'w') as f:
        prints, informs = generate_dataset()
        prints_header = "## intent:print"
        inform_header = "## intent:inform"
        f.write(prints_header+"\n")
        for index, intents in prints.items():
            for intent in intents:
                if random.random() < 0.3:
                    f.write("- "+intent+"\n")

        f.write(inform_header + "\n")
        for index, intents in informs.items():
            for intent in intents:
                if random.random() < 0.3:
                    f.write("- "+intent+"\n")

        f.close()


generate_md_file()
