#!/usr/bin/env python

import os
from setuptools import find_packages, setup

ENCODING = 'utf-8'
PACKAGE_NAME = 'pgawedge'

local_directory = os.path.abspath(os.path.dirname(__file__))
version_path = os.path.join(local_directory, PACKAGE_NAME, '_version.py')

version_ns = {}
with open(version_path, 'r', encoding=ENCODING) as f:
    exec(f.read(), {}, version_ns)


def get_requirements(requirement_file):
    requirements = list(
        open(requirement_file, 'r',
             encoding=ENCODING).read().strip().split('\r\n'))
    return requirements


setup(name=PACKAGE_NAME,
      packages=find_packages(exclude=('tests',)),
      package_data={
          '': ['*.txt', '*.sql', '*.json'],
      },
      include_package_data=True,
      version=version_ns['__version__'],
      license='BSD',
      description='sqlalchemy postgresql adapter and utilities.',
      url='https://github.com/portfoliome/pgawedge',
      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Database',
          'Topic :: Database :: Database Engines/Servers',
          'Topic :: Utilities',
          'Development Status :: 4 - Beta'
      ],
      author='Philip Martin',
      author_email='philip.martin@censible.co',
      install_requires=get_requirements('requirements.txt'),
      extras_require={
          'develop': get_requirements('requirements-dev.txt'),
          'test': get_requirements('requirements-test.txt')
      },
      zip_safe=False)
