__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

class EnTKError(Exception):
	"""EnTKError is the base exception thrown by the Ensemble Toolkit"""
	def __init__ (self, msg):
		super(EnTKError, self).__init__ (msg)


class TypeError(EnTKError):
	"""TypeError is thrown if a parameter of a wrong type is passed to a method or function."""

	def __init__ (self, expected_type, actual_type):
		msg = "Expected (base) type {0}, but got {1}.".format(
			str(expected_type), 
			str(actual_type)
			)
		super(TypeError, self).__init__ (msg)

class MatchError(EnTKError):
	"""MatchError is thrown if two parameters are not equal."""

	def __init__ (self, par1, par2):
		msg = "{0} does not match {1}.".format(
			str(par1), 
			str(par2)
			)
		super(MatchError, self).__init__ (msg)

class ArgumentError(EnsemblemdError):
	"""A BadArgumentError is thrown if a wrong set of arguments were passed 
	to a kernel.
	"""
	def __init__ (self, kernel_name, message, valid_arguments_set):
		msg = "Invalid argument(s) for kernel '{0}': {1}. Valid arguments are {2}.".format(
			kernel_name,
			message,
			valid_arguments_set
			)
		super(ArgumentError, self).__init__ (msg)


class NotImplementedError(EnsemblemdError):
	"""NotImplementedError is thrown if a class method or function is not 
	implemented."""

	def __init__ (self, method_name, class_name):
		msg = "Method {0}() missing implementation in {1}.".format(
			method_name, 
			class_name
			)
		super(NotImplementedError, self).__init__ (msg)