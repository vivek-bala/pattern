__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.patterns.errors.exceptions import *
from radical.patterns.execution_pattern import ExecutionPattern

class EoP(ExecutionPattern):

	def __init__(self, stages, instances, type='unit', object_list=None, iteration = False):

		self._stages = stages
		self._instances = instances
		self._type = type
		self._object_list = object_list
		self._iteration = iteration

		# Perform sanity check -- perform before proceeding
		self.sanity_check()


	def sanity_check(self):

		# Check type errors
		if type(self._stages) != int:
			raise TypeError(expected_type=int, actual_type=type(self._stages))

		if type(self._instances) != int:
			raise TypeError(expected_type=int, actual_type=type(self._instances))

		if type(self._type) != str:
			raise TypeError(expected_type=str, actual_type=type(self._type))		

		if ((type(self._object_list) != list) and (self._object_list != None)):
			raise TypeError(expected_type=list, actual_type=type(self._object_list))

		if type(self._iteration) != bool:
			raise TypeError(expected_type=bool, actual_type=type(self._iteration))


		# Check value errors
		if ((self._type != 'unit') and (self._type != 'complex')):
			raise ValueError(expected_value=['unit','complex'], actual_value=self._type)

		# Check match errors

		## Test if number of stages == length of object_list
		if ((self._type != 'unit') and (self.stages != len(self.object_list))):
			raise MatchError(par1="stages", par2="number of objects")



	@property
	def stages(self):
		return self._stages

	@property
	def instances(self):
		return self._instances

	@property
	def object_list(self):
		return self._object_list

	@property
	def iteration(self):
		return self._iteration
	
	@property
	def type(self):
		return self._type
	