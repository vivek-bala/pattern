__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.patterns import EoP
from radical.patterns import AppManager
from radical.patterns import Kernel

from hello import hello_kernel

class Test(EoP):

	def __init__(self, ensemble_size, pipeline_size):
		super(Test,self).__init__(ensemble_size, pipeline_size)

	def stage_1(self, instance):
		k1 = Kernel(name="hello")

		return k1

	def branch_1(self):

		if (stage_1['instace_1'].status == 'Failed'):
			self.next_stage = 3
		elif (stage_1['instance_1'].output > 1):
			# Do something
		else:
			pass
		

	def stage_2(self,instance):

		k2 = Kernel(name='new')
		return k2

	'''
	def branch_2(self):
		# Do something

	'''

	def stage_3(self,instance):

		k3 = Kernel(name="world")

		return k3



if __name__ == '__main__':

	pipe = Test(ensemble_size=16, pipeline_size=1)
	#ensemble = Ensemble(tasks=2, object_list=[pipe])

	app = AppManager(name='firstapp')
	#print app.name

	app.register_kernels(hello_kernel)
	kerns = app.get_kernels()

	app.run(pipe)
	#print kerns
	#print app
