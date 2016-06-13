__author__    = "Vivek Balasubramanian <vivek.balasubramanian@rutgers.edu>"
__copyright__ = "Copyright 2016, http://radical.rutgers.edu"
__license__   = "MIT"

import os
import sys
from setuptools import setup, find_packages, Command


srcroot = os.path.dirname(os.path.realpath(__file__))
#check_version()
#short_version, long_version = get_version()

setup_args = {
	'name'             : 'radical.patterns',
	'version'          : '0.1',
	'description'      : "Patterns",
	'author'           : 'RADICAL Group at Rutgers University',
	'author_email'     : 'vivek.balasubramanian@rutgers.edu',
	'url'              : 'https://github.com/vivek-bala/patterns',
	'license'          : 'MIT',
	'keywords'         : "execution patterns for control and dataflow applications",
	'classifiers'      :  [
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Environment :: Console',
		'License :: OSI Approved :: MIT License',
		'Topic :: Utilities',
		'Topic :: System :: Software Design',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: POSIX',
		'Operating System :: Unix'
	],

	#'entry_points': {
	#    'console_scripts':
	#        ['htbac-fecalc = radical.ensemblemd.htbac.bin.fecalc:main',
	#         'htbac-sim    = radical.ensemblemd.htbac.bin.sim:main']
	#},

	'namespace_packages': ['radical','radical'],
	'packages'          : find_packages('src'),
	'package_dir'       : {'': 'src'},
}

setup (**setup_args)
