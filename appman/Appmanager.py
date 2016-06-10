__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

from errors.exceptions import *

class AppManager():

	def __init__(self, pattern):

		self._pattern = pattern

		# Uncomment once ExecutionPattern class is available
		#self.sanity_check()

	def sanity_check(self):

		if type(self._pattern) != "ExecutionPattern":
			raise TypeError(expected_type="ExecutionPattern", actual_type=type(self._pattern))

