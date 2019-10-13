import re
import random


def load_objects(path):
    return [f[:-1] for f in open(path,'r').readlines()]


if __name__ == "__main__":
    OBJECT = 'objects.txt'
    COLORS = 'colors.txt'
    SIZES = 'sizes.txt'

    
