__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.patterns import PoE
from radical.patterns import AppManager
from radical.patterns import Kernel

from hello import hello_kernel

class Test(PoE):

	def __init__(self, ensemble_size, pipeline_size, iterations):
		super(Test,self).__init__(ensemble_size, pipeline_size, iterations)

	def stage_1(self, instance):
		k1 = Kernel(name="hello_module")
		k1.cores = 3
		return k1


	def branch_1(self):
		print self.cur_iteration
		
	


if __name__ == '__main__':

	pipe = Test(ensemble_size=16, pipeline_size=1, iterations=2)
	#ensemble = Ensemble(tasks=2, object_list=[pipe])

	app = AppManager(name='firstapp')
	#print app.name

	app.register_kernels(hello_kernel)
	kerns = app.list_kernels()

	app.run(pipe)
	#print kerns
	#print app
