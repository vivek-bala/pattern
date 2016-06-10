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