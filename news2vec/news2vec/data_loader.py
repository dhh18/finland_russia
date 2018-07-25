import pickle
from . import w2v

pickle_path_federal = 'models/model_integrum_federal_sg0_mc1.pkl'
pickle_path_local = 'models/model_integrum_local_sg0_mc1.pkl'

print("Loading models from {}".format(pickle_path_federal))
models_federal = pickle.load(open(pickle_path_federal, "rb"))
print("Loading models from {}".format(pickle_path_local))
models_local = pickle.load(open(pickle_path_local, "rb"))

models = {}
models['integrum_federal'] = w2v.W2VModel(models_federal)
models['integrum_local'] = w2v.W2VModel(models_local)
