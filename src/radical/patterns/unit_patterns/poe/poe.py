__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.patterns.errors.exceptions import *
from radical.patterns.execution_pattern import ExecutionPattern

class PoE(ExecutionPattern):

	def __init__(self, tasks, object_list):

		self._tasks = tasks
		self._object_list = object_list

		# Perform sanity check -- perform before proceeding
		self.sanity_check()


	def sanity_check(self):

		# Check value type for stages
		if type(self._tasks) != int:
			raise TypeError(expected_type=int, actual_type=type(self._tasks))

		if type(self._object_list) != list:
			raise TypeError(expected_type=list, actual_type=type(self._object_list))

		# Test if number of stages == length of object_list
		if ((self.tasks != len(self._object_list)) and (len(self._object_list)!=1)):
			raise MatchError(par1="tasks", par2="number of objects")

	@property
	def tasks(self):
		return self._tasks
	
	@property
	def object_list(self):
		return self._object_list
