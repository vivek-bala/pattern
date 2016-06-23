__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.patterns import EoP
from radical.patterns import AppManager
from radical.patterns import Kernel

from hello import hello_kernel

class Test(EoP):

	def __init__(self,stages, instances):
		super(Test,self).__init__(stages,instances)

	def stage_1(self, instance):
		k1 = Kernel(name="hello")

		return k1



if __name__ == '__main__':

	pipe = Test(stages=1, instances=16)
	#ensemble = Ensemble(tasks=2, object_list=[pipe])

	app = AppManager(name='firstapp')
	#print app.name

	app.register_kernels(hello_kernel)
	kerns = app.get_kernels()

	app.run(pipe)
	#print kerns
	#print app
