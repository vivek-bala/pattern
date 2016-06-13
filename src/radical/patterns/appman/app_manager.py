__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.patterns.errors.exceptions import *
from radical.patterns.kernel_plugins.kernel import Kernel

class AppManager():

	def __init__(self, name=None):

		self._name = name

		self._pattern = None
		self._loaded_kernels = list()

		# Uncomment once ExecutionPattern class is available
		#self.sanity_check()

	def sanity_check(self):

		if type(self._pattern) != "ExecutionPattern":
			raise TypeError(expected_type="ExecutionPattern", actual_type=type(self._pattern))

	@property
	def name(self):
		return self._name
	
	def get_name(self):
		return self._name
		

	def register_kernels(self, kern):

		if type(kern) == list:
			self._loaded_kernels.extend(kern)
		elif type(kern) == Kernel:
			self._loaded_kernels.append(kern)
		else:
			raise TypeError(expected_type="Kernel", actual_type = type(kern))


	def get_kernels(self):

		registered_kernels = list()
		for item in self._loaded_kernels:
			registered_kernels.append(item.name)

		return registered_kernels