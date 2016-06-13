__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.patterns import EoP
from radical.patterns import AppManager
from radical.patterns import Kernel

from hello import hello_kernel

if __name__ == '__main__':

	pipe = EoP(stages=3)
	#ensemble = Ensemble(tasks=2, object_list=[pipe])

	k1 = Kernel(name="test")

	app = AppManager(name='firstapp')
	#print app.name
	app.register_kernels(k1)
	app.register_kernels(k1)
	kerns = app.get_kernels()

	print kerns
	#print app
