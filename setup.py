#!/usr/bin/env python3

from distutils.core import setup
from os import path

from buildutil.version import __version__
from buildutil.version import __license__
from buildutil.version import __author__
from buildutil.version import __email__

here = path.abspath(path.dirname(__file__))

# ------------------------------------------------------------------------------

# Package name
name = "buildutil"

# Import version info
exec(open(path.join(here, '{}/version.py'.format(name))).read())

# Long description
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

# ------------------------------------------------------------------------------
# Setup config
setup(
	name=name,
	packages=[name],
	version=__version__,
	license=__license__,
	description='Build utils',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author=__author__,
	author_email=__email__,
	url='https://github.com/tedicreations/buildutil',
	download_url='https://github.com/TediCreations/buildutil/archive/' + __version__ + '.tar.gz',
	keywords=['build', 'make', 'util'],
	install_requires=[
		'argparse-color-formatter',
	],
	package_data={'buildutil': ['conf/make/*']},
	include_package_data=True,
	entry_points={
		"console_scripts": [
			"buildutil = buildutil.main:main",
		]
	},
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
	],
)
