#!/usr/bin/env python

"""This module defines and implements the Kernel class.
"""

__author__    = "Vivek Balasubramanian <vivek.balasubramaninan@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from radical.patterns.errors.exceptions import *

# ------------------------------------------------------------------------------
#
class Kernel(object):

	#---------------------------------------------------------------------------
	#
	def __init__(self, name, args=None,instance_type=None):
		"""Create a new Kernel object.
		"""
		if type(name) != str:
			raise TypeError(
				expected_type=str,
				actual_type=type(name))

		self._name = name
		#self._engine = Engine()
		#self._kernel = self._engine.get_kernel_plugin(name)

		#if args is not None:
		#	self.set_args(args)			

	
	#---------------------------------------------------------------------------
	@property
	def pre_exec(self):
		return self._kernel._pre_exec

	@pre_exec.setter
	def pre_exec(self, commands):
		self._kernel._pre_exec = commands
	#---------------------------------------------------------------------------

	@property
	def _cu_def_post_exec(self):
		return self._kernel._post_exec
	#---------------------------------------------------------------------------

	@property
	def post_exec(self):
		return self._kernel._post_exec

	@post_exec.setter
	def post_exec(self, commands):
		self._kernel._post_exec = commands
	#---------------------------------------------------------------------------

	@property
	def name(self):
		#return self._kernel.get_name()
		return self._name
	#---------------------------------------------------------------------------

	@property
	def _cu_def_output_data(self):
		return self._kernel._download_output_data

	#---------------------------------------------------------------------------

	@property
	def _cu_def_input_data(self):
		return self._kernel._upload_input_data
	#---------------------------------------------------------------------------

	@property
	def _cu_def_executable(self):
		return self._kernel._executable
	#---------------------------------------------------------------------------

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
	#---------------------------------------------------------------------------

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

		# Call the validate_args() method of the plug-in.
		self._kernel.validate_args(args)
	#---------------------------------------------------------------------------

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

		# Call the validate_args() method of the plug-in.
		self._kernel._cores = cores
	#---------------------------------------------------------------------------

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
	#---------------------------------------------------------------------------

	@property
	def download_input_data(self):
		return self._kernel._download_input_data

	@download_input_data.setter
	def download_input_data(self, data_directives):

		if type(data_directives) != list:
			data_directives = [data_directives]

		for dd in data_directives:
			if type(dd) != str:
				raise TypeError(
					expected_type=str,
					actual_type=type(dd))

		self._kernel._download_input_data = data_directives
	#---------------------------------------------------------------------------
	#
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
	#---------------------------------------------------------------------------
	#
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
	#---------------------------------------------------------------------------
	#
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

	#---------------------------------------------------------------------------
	#
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
	#---------------------------------------------------------------------------
	#
	def get_raw_args(self):
		return self._kernel.get_arg(name)

	#---------------------------------------------------------------------------
	#
	def get_arg(self, name):
		return self._kernel.get_arg(name)


	#---------------------------------------------------------------------------
	#
	@property
	def get_instance_type(self):
		return self._kernel.instance_type
	#---------------------------------------------------------------------------
	#
	def _bind_to_resource(self, resource_key, pattern_name=None):
		"""Returns the kernel description as a dictionary that can be
		   translated into a CU description.
		"""
		raise NotImplementedError(
		  method_name="_get_kernel_description",
		  class_name=type(self))