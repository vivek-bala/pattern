__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.patterns.errors.exceptions import *
from radical.patterns.execution_pattern import ExecutionPattern
import pprint

class PoE(ExecutionPattern):

	def __init__(self, ensemble_size, pipeline_size, iterations = 1, type='unit', iterative = False):

		self._ensemble_size = ensemble_size
		self._pipeline_size = pipeline_size
		self._type = type
		self._total_iterations = iterations
		self._iterative = iterative

		# Internal parameters
		self._next_stage = 1
		self._cur_iteration = 1
		self.kill_instances = None

		# Perform sanity check -- perform before proceeding
		self.sanity_check()

		self._kernel_dict = dict()

	def sanity_check(self):

		# Check type errors
		if type(self._pipeline_size) != int:
			raise TypeError(expected_type=int, actual_type=type(self._ensemble_size))

		if type(self._ensemble_size) != int:
			raise TypeError(expected_type=int, actual_type=type(self._pipeline_size))
		elif ((type(self._ensemble_size) != list) and (type(self._ensemble_size) != int)):
			raise TypeError(expected_type=list, actual_type=type(self._pipeline_size))

		if type(self._type) != str:
			raise TypeError(expected_type=str, actual_type=type(self._type))		

		if type(self._total_iterations) != int:
			raise TypeError(expected_type=int, actual_type=type(self._total_iterations))

		if type(self._iterative) != bool:
			raise TypeError(expected_type=bool, actual_type=type(self._iterative))


		# Check value errors
		if ((self._type != 'unit') and (self._type != 'complex')):
			raise ValueError(expected_value=['unit','complex'], actual_value=self._type)

	@property
	def ensemble_size(self):
		return self._ensemble_size
	
	@property
	def pipeline_size(self):
		return self._pipeline_size

	@property
	def total_iterations(self):
		return self._total_iterations
	

	@property
	def cur_iteration(self):
		return self._cur_iteration

	@cur_iteration.setter
	def cur_iteration(self, cur_iteration):
		self._cur_iteration = cur_iteration

	@property
	def next_stage(self):
		return self._next_stage
	
	@next_stage.setter
	def next_stage(self, next_stage):
		self._next_stage = next_stage
	
	@property
	def type(self):
		return self._type

	@property
	def iterative(self):
		return self._iterative
	
	
	def create_record(self):

		for iter in range(1, self._total_iterations+1):
			self._kernel_dict["iter_{0}".format(iter)] = dict()

			for stage in range(1, self._pipeline_size+1):
				self._kernel_dict["iter_{0}".format(iter)]["stage_{0}".format(stage)]  = dict()

				# Set kernel default status
				self._kernel_dict["iter_{0}".format(iter)]["stage_{0}".format(stage)]['status'] = 'New'

				# Set available branches
				if getattr(self,'branch_{0}'.format(stage), False):
					self._kernel_dict["iter_{0}".format(iter)]["stage_{0}".format(stage)]['branch'] = True
				else:
					self._kernel_dict["iter_{0}".format(iter)]["stage_{0}".format(stage)]['branch'] = False
		

				# Create instance key/vals for each stage
				if type(self._ensemble_size) == int:
					instances = self._ensemble_size
				elif type(self._ensemble_size) == list:
					instances = self._ensemble_size[stage-1]

				for inst in range(1, instances+1):
					self._kernel_dict["iter_{0}".format(iter)]["stage_{0}".format(stage)]["instance_{0}".format(inst)] = dict()
					self._kernel_dict["iter_{0}".format(iter)]["stage_{0}".format(stage)]["instance_{0}".format(inst)]["output"] = None
					self._kernel_dict["iter_{0}".format(iter)]["stage_{0}".format(stage)]["instance_{0}".format(inst)]["uid"] = None
					self._kernel_dict["iter_{0}".format(iter)]["stage_{0}".format(stage)]["instance_{0}".format(inst)]["status"] = None



		# Print empty dict to check structure					
		#pprint.pprint(self._kernel_dict)


	def get_record(self):
		return self._kernel_dict

	def get_stage(self, stage):

		stage_kernel = getattr(self, "stage_{0}".format(stage), None)

		if stage_kernel == None:
			raise Exception("Pattern does not have stage_{0}".format(stage))

		'''
		if instance == None:

			kernel_list = list()

			# Create instance key/vals for each stage
			if type(self._ensemble_size) == int:
				instances = self._ensemble_size
			elif type(self._ensemble_size) == list:
				instances = self._ensemble_size[stage-1]


			for inst in range(1, instances):

				kernel_list.append(stage_kernel(inst))

		else:

			return stage_kernel(instance)
		'''

		return stage_kernel


	def get_branch(self, stage):

		branch = getattr(self, "branch_{0}".format(stage), None)

		if branch == None:
			raise Exception("Pattern does not have branch_{0}".format(stage))

		return branch