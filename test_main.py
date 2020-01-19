from apexio import generate_Infersent_model, generate_models
from apexio_prediction import make_predictions
import os

def grab_files(path):
	files = []
	for r, d, f in os.walk(path):
		for file in f:
			files.append(os.path.join(r, file))
	return files

files = grab_files('./TestSources/')

model = generate_Infersent_model()
dir_triples = [
	('./TestTargets/AMS', 'AMS', './models/AMS_model.h5'),
	('./TestTargets/English', 'English', './models/English_model.h5'),
	('./TestTargets/Science', 'Science', './models/Science_model.h5'),
	('./TestTargets/WesternCiv', 'WesternCiv', './models/WesternCiv_model.h5'),
]
#model_locs = generate_models(dir_triples, model)

recs = make_predictions(dir_triples, files, model)

print(recs)
