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
	('./TestTargets/AMS', 'AMS'),
	('./TestTargets/CollegeApps', 'CollegeApps'),
	('./TestTargets/Core1', 'Core1'),
	('./TestTargets/Crown92', 'Crown92'),
	('./TestTargets/CS70', 'CS70'),
	('./TestTargets/English', 'English'),
	('./TestTargets/History', 'History'),
	('./TestTargets/Science', 'Science'),
	('./TestTargets/WesternCiv', 'WesternCiv'),
	('./TestTargets/Writing2', 'Writing2')
]
model_locs = generate_models(dir_triples, model)
new_triples = []
for i in range(len(model_locs)):
	tri = dir_triples[i]
	new_triples.append((tri[0],tri[1],model_locs[i]))


recs = make_predictions(new_triples, files)

print(recs)
