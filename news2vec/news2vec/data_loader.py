import pickle
from . import w2v

pickle_path_federal = 'models/integrum_federal_word_models.pkl'
pickle_path_local = 'models/integrum_local_word_models.pkl'

print("Loading models from {}".format(pickle_path_federal))
models_federal = pickle.load(open(pickle_path_federal, "rb"))
print("Loading models from {}".format(pickle_path_local))
models_local = pickle.load(open(pickle_path_local, "rb"))

models = {}
models['integrum_federal'] = w2v.W2VModel(models_federal)
models['integrum_local'] = w2v.W2VModel(models_local)
