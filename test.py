from unit_patterns.poe.pipeline import Pipeline
from unit_patterns.eop.ensemble import Ensemble

if __name__ == '__main__':

	pipe = Pipeline(stages=3, object_list=['a','b','c'])
	ensemble = Ensemble(tasks=2, object_list=[pipe])

	print pipe
	print ensemble
