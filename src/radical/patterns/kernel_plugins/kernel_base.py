#!/usr/bin/env python

"""Defines and implements the abstract kernel base class.
"""

__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from copy import deepcopy

from radical.patterns.errors.exceptions import *

# ------------------------------------------------------------------------------ --------------------------------------------------------
# Kernel format
"""
_KERNEL_INFO = {
	"name":         "kernel name",
	"description":  "Description about kernel",
	"arguments":   {
				"--arg1=":
				{
					"mandatory": False,
					"description": "argument description"
				}
			},
	"machine_configs": 
			{
				"resource_name": {
					"pre_exec"      : [],
					"executable"    : "",
					"uses_mpi"      : False
				},
			}
	}
"""
#  ------------------------------------------------------------- ------------------------------------------------------------------------------

#  ------------------------------------------------------------- ------------------------------------------------------------------------------
# plugin base class
#
class KernelBase(object):

	#  ------------------------------------------------------------- ------------------------------------------------------------------------------
	
	def __init__ (self, kernel_info) :

		self._kernel_info     = kernel_info
		self._kernel_name     = kernel_info['name']

		if 'description' in kernel_info:
			self._kernel_description  = kernel_info['description']

		self._args     = []
		self._raw_args = []

		# No use-case but can be supported
		# Parameters required for any Kernel irrespective of RP
		self._pre_exec               	= None
		self._executable 	= None
		self._arguments       	= None
		self._uses_mpi               = None
		self._input_staging 	= None
		self._output_staging 	= None
		self._cores                  	= 1 # If unspecified, number of cores is set to 1
	#  ------------------------------------------------------------- ------------------------------------------------------------------------------
	
	def as_dict(self):
		"""Returns a dictionary representation of the kernel"""
	
		kernel_dict = {	"pre_exec": 	self._pre_exec,
			 	"executable": 	self._executable,
			 	"arguments": 	self._arguments,
			 	"uses_mpi": 	self._uses_mpi,
			 	"input_data":	self._input_staging,
			 	"output_data":  self._output_staging,
			 	"cores": 	self._cores
			 	}

		return kernel_dict
	# ------------------------------------------------------------- ------------------------------------------------------------------------------
	
	@property
	def name(self):
		return self._kernel_name
	
	def get_name():
		return self._name
	# ------------------------------------------------------------- ------------------------------------------------------------------------------

	@property
	def kernel_info(self):
		return self._kernel_info
	
	def get_kernel_info (self) :
		return self._kernel_info
	# ------------------------------------------------------------- ------------------------------------------------------------------------------
	
	def get_arg(self, arg_name):
		"""Returns the value of the argument given by 'arg_name'.
		"""
		return self._args[arg_name]["_value"]
	# ------------------------------------------------------------- ------------------------------------------------------------------------------
	
	def get_raw_args(self):
		"""Returns all arguments as they were passed to the kernel.
		"""
		return self._raw_args

	# ------------------------------------------------------------- ------------------------------------------------------------------------------
	# ------------------------------------------------------------- ------------------------------------------------------------------------------
	# Methods to get via API

	@property
	def executable(self):
		return self._executable

	@property
	def pre_exec(self):
		return self._pre_exec
	# ------------------------------------------------------------- ------------------------------------------------------------------------------
	# ------------------------------------------------------------- ------------------------------------------------------------------------------
	# Methods to set kernel parameters via API

	# uses_mpi
	# arguments
	# cores
	# upload_input_data
	# link_input_data
	# copy_input_data
	# download_output_data
	# copy_output_data
	
	# ------------------------------------------------------------- ------------------------------------------------------------------------------
	
	@property
	def uses_mpi(self):
		return self._kernel._uses_mpi

	@uses_mpi.setter
	def uses_mpi(self, uses_mpi):

		if type(uses_mpi) != bool:
			raise TypeError(
				expected_type=bool,
				actual_type=type(uses_mpi))

		# Call the validate_args() method of the plug-in.
		self._kernel._uses_mpi = uses_mpi
	# ------------------------------------------------------------- ------------------------------------------------------------------------------

	@property
	def arguments(self):
		"""List of arguments to the kernel as defined by the kernel definition files"""
		return self._kernel._arguments

	@arguments.setter
	def arguments(self, args):
		"""Sets the arguments for the kernel.
		"""
		if type(args) != list:
			raise TypeError(
				expected_type=list,
				actual_type=type(args))

		self._kernel.validate_args(args)
	# ------------------------------------------------------------- ------------------------------------------------------------------------------

	@property
	def cores(self):
		"""The number of cores the kernel is using.
		"""
		return self._kernel._cores

	@cores.setter
	def cores(self, cores):

		if type(cores) != int:
			raise TypeError(
				expected_type=int,
				actual_type=type(cores))

		self._kernel._cores = cores
	# ------------------------------------------------------------- ------------------------------------------------------------------------------

	@property
	def upload_input_data(self):
		return self._kernel._upload_input_data

	@upload_input_data.setter
	def upload_input_data(self, data_directives):
		if type(data_directives) != list:
			data_directives = [data_directives]

		for dd in data_directives:
			if type(dd) != str:
				raise TypeError(
					expected_type=str,
					actual_type=type(dd))

		self._kernel._upload_input_data = data_directives
	# ------------------------------------------------------------- ------------------------------------------------------------------------------

	@property
	def link_input_data(self):
		return self._kernel._link_input_data

	@link_input_data.setter
	def link_input_data(self, data_directives):
		if type(data_directives) != list:
			data_directives = [data_directives]

		for dd in data_directives:
			if type(dd) != str:
				raise TypeError(
					expected_type=str,
					actual_type=type(dd))

		self._kernel._link_input_data = data_directives
	# ------------------------------------------------------------- ------------------------------------------------------------------------------

	@property
	def copy_input_data(self):
		return self._kernel._copy_input_data

	@copy_input_data.setter
	def copy_input_data(self, data_directives):

		if type(data_directives) != list:
			data_directives = [data_directives]

		for dd in data_directives:
			dd = str(dd)
			if type(dd) != str:
				raise TypeError(
					expected_type=str,
					actual_type=type(dd))

		self._kernel._copy_input_data = data_directives
	# ------------------------------------------------------------- ------------------------------------------------------------------------------

	@property
	def download_output_data(self):
		return self._kernel._download_output_data

	@download_output_data.setter
	def download_output_data(self, data_directives):

		if type(data_directives) != list:
			data_directives = [data_directives]

		for dd in data_directives:
			if type(dd) != str:
				raise TypeError(
					expected_type=str,
					actual_type=type(dd))

		self._kernel._download_output_data = data_directives
	# ------------------------------------------------------------- ------------------------------------------------------------------------------

	@property
	def copy_output_data(self):
		return self._kernel._copy_output_data

	@copy_output_data.setter
	def copy_output_data(self, data_directives):

		if type(data_directives) != list:
			data_directives = [data_directives]

		for dd in data_directives:
			if type(dd) != str:
				raise TypeError(
					expected_type=str,
					actual_type=type(dd))

		self._kernel._copy_output_data = data_directives
	# ------------------------------------------------------------- ------------------------------------------------------------------------------


	# ------------------------------------------------------------- ------------------------------------------------------------------------------
	#
	# Method for validating given arguments are expected from Kernel Info

	def validate_args(self, args):
		"""Validates if 'args' fulfill the argument requirements defined in the
		   kernel info.
		"""
		self._raw_args = args

		arg_config = deepcopy(self._info['arguments'])

		if arg_config == "*":
			self._args = args
			#self.get_logger().debug("Free-form argument validation ok: {0}.".format(args))
			return

		for (arg, arg_info) in arg_config.iteritems():
			arg_config[arg]["_is_set"] = False
			arg_config[arg]["_value"] = None

		# Check if only valid args are passed.
		for kernel_arg in args:
			kernel_arg_ok = False
			for (arg, arg_info) in arg_config.iteritems():
				if kernel_arg.startswith(arg):
					kernel_arg_ok = True
					arg_config[arg]["_is_set"] = True
					arg_config[arg]["_value"] = kernel_arg.replace(arg, '')
					break

			if kernel_arg_ok is False:
				raise ArgumentError(
					kernel_name=self.get_name(),
					message="Unknown / malformed argument '{0}'".format(kernel_arg),
					valid_arguments_set=arg_config
				)

		# Check if mandatory args are set.
		for (arg, arg_info) in arg_config.iteritems():
			if (arg_info["mandatory"] == True) and (arg_info["_is_set"] == False):
				raise ArgumentError(
					kernel_name=self.get_name(),
					message="Mandatory argument '{0}' missing".format(arg),
					valid_arguments_set=self._info['arguments']
				)

		#self.get_logger().debug("Arguments ok: {0}.".format(args))
		self._args = arg_config
	# ------------------------------------------------------------- ------------------------------------------------------------------------------

	def _bind_to_resource(self, resource_key, pattern_name=None):
		"""Binds the kernel to a specific resource.
		"""
		raise NotImplementedError(
		  method_name="_get_kernel_description",
		  class_name=type(self))
	# ------------------------------------------------------------- ------------------------------------------------------------------------------