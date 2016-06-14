__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.patterns import EoP
from radical.patterns import AppManager
from radical.patterns import Kernel

from hello import hello_kernel

class Test(EoP):

	def __init__(self,stages, instances):
		EoP.__init__(self, stages, instances)

	def stage_1(self, instance):
		k1 = Kernel(name="hello")



if __name__ == '__main__':

	pipe = Test(stages=1, instances=16)
	#ensemble = Ensemble(tasks=2, object_list=[pipe])

	app = AppManager(name='firstapp')
	#print app.name
	app.register_kernels(k1)
	app.register_kernels(k1)
	kerns = app.get_kernels()

	print kerns
	#print app
