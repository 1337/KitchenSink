from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='KitchenSink',
      version=version,
      description="Like utils, but for every project.",
      long_description="",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Brian Lai',
      author_email='brian@ohai.ca',
      url='http://ohai.ca',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
