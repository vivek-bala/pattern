__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.patterns.errors.exceptions import *
from radical.patterns.kernel_plugins.kernel_base import Kernel
from radical.patterns.appman.plugin_registry import default_plugins
from radical.patterns.execution_pattern import ExecutionPattern

class AppManager():

	def __init__(self, name=None):

		self._name = name

		self._pattern = None
		self._loaded_kernels = list()
		self._loaded_plugins = list() 

		# Uncomment once ExecutionPattern class is available
		#self.sanity_check()

		# Load default exec plugins
		self.load_plugins()

	def sanity_pattern_check(self):
		if self._pattern.__class__.__base__.__base__ != ExecutionPattern:
			raise TypeError(expected_type="(derived from) ExecutionPattern", actual_type=type(self._pattern))

	@property
	def name(self):
		return self._name

	def load_plugins(self):

		# Load default execution plugins
		for plugin in default_plugins:

			adaptor_module = None
			# attempt to load exec plugin 
			try :
				adaptor_module = __import__ (plugin, fromlist=['Plugin'])

			except Exception as e:
				# plugin load failed
				continue

	

	def register_kernels(self, kernel_class):

		#print kernel_class.__base__
		if type(kernel_class) == list:
			for item in kernel_class:
				if not hasattr(item, '__base__'):
					raise TypeError(expected_type="Kernel", actual_type = type(item))					
				elif item.__base__ != Kernel:
					raise TypeError(expected_type="Kernel", actual_type = type(item()))		

				if item in self._loaded_kernels:
					raise ExistsError(item='{0}'.format(item().name), parent = 'loaded_kernels')

				self._loaded_kernels.append(item)

		elif not hasattr(kernel_class,'__base__'):
			raise TypeError(expected_type="Kernel", actual_type = type(kernel_class))

		elif kernel_class.__base__ != Kernel:
			raise TypeError(expected_type="Kernel", actual_type = type(kernel_class()))

		else:
			self._loaded_kernels.append(kernel_class)
		


	def get_kernels(self):

		registered_kernels = list()
		for item in self._loaded_kernels:
			registered_kernels.append(item().name)

		return registered_kernels

	def save(self, pattern):
		self._pattern = pattern
		self.sanity_pattern_check()

		# Convert pattern to JSON
		self.pattern_to_json(pattern)

	def pattern_to_json(self, pattern):
		pass

	def run(self, pattern):

		print pattern.__class__.__base__