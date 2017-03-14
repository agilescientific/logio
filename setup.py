# -*- coding: utf 8 -*-
"""
Python installation file for logio.
"""
from setuptools import setup
import re

verstr = 'unknown'
VERSIONFILE = "logio/_version.py"
with open(VERSIONFILE, "r")as f:
    verstrline = f.read().strip()
    pattern = re.compile(r"__version__ = ['\"](.*)['\"]")
    mo = pattern.search(verstrline)
if mo:
    verstr = mo.group(1)
    print("Version "+verstr)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

REQUIREMENTS = ['numpy',
                'cython',
                'matplotlib',
                ]

TEST_REQUIREMENTS = ['pytest',
                     'coveralls',
                     'pytest-cov',
                     'pytest-mpl',
                     ]

# Test command is:
# py.test --mpl --cov striplog

CLASSIFIERS = ['Development Status :: 3 - Alpha',
               'Intended Audience :: Science/Research',
               'Natural Language :: English',
               'License :: OSI Approved :: Gnu Public License',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               ]

setup(name='logio',
      version=verstr,
      description='Tools for loading well data.',
      url='http://github.com/agile-geoscience/logio',
      author='Agile Geoscience',
      author_email='hello@agilegeoscience.com',
      license='GPL',
      packages=['logio'],
      tests_require=TEST_REQUIREMENTS,
      test_suite='run_tests',
      install_requires=REQUIREMENTS,
      classifiers=CLASSIFIERS,
      zip_safe=False,
      )

