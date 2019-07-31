#!/usr/bin/env python

import os
from distutils.core import setup
import subprocess

# convert readme to rst format
try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except:
   long_description = ''

versionfile = "pygame-text-input/version.py"
if not os.path.isfile(versionfile):
    # assume git checkout
    __version__ = str(subprocess.check_output(["git", "describe", "--tag", "--always"])).strip("\n")
else:
    # created by pip
    exec(open(versionfile).read())

setup(
    version=__version__,
    name='pygame-text-input',
    description='pygame text input box',
    long_description=long_description,
    author='Silas Gyger',
    author_email='silasgyger@gmail.com',
    url='https://github.com/Nearoo/pygame-text-input',
    packages=['pygame-text-input'],
)
