#!/usr/bin/env python

import sys
if 'build_sphinx' in sys.argv or 'develop' in sys.argv:
    from setuptools import setup, Command
else:
    from distutils.core import setup, Command

with open('README.rst') as file:
    long_description = file.read()

with open('CHANGES') as file:
    long_description += file.read()

# no versions yet from agpy import __version__ as version

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

execfile('starlink_wrappers/version.py')

import glob 
scripts = [fname for fname in glob.glob(os.path.join('scripts', '*'))
            if os.path.basename(fname) != 'README.rst']

setup(name='starlink_wrappers',
      scripts=scripts,
      version=__version__,
      description='Wrappers for STARLINK tools to work "directly" on FITS files',
      long_description=long_description,
      author='Adam Ginsburg',
      author_email='adam.g.ginsburg@gmail.com',
      url='https://github.com/keflavich/starlink_wrappers',
      packages=['starlink_wrappers'], 
      cmdclass = {'test': PyTest},
     )
