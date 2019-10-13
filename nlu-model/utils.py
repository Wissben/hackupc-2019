from rasa_nlu.model import Interpreter
MODEL_DIR = './models/nlu/'
# where model_directory points to the model folder
interpreter = Interpreter.load(MODEL_DIR)
interpreter.parse(u"The text I want to understand")

