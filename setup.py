#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

setup(name='pykoreaqi',
	  version='0.1.0',
	  description='Scrapes Korean Air Quality (http://www.airkorea.or.kr) data',
	  author='Chris Ochoa',
	  author_email='cochoa0x1@gmail.com',
	  packages=['pykoreaqi'],
	  license='MIT',
	  url='https://github.com/cochoa0x1/pykoreaqi',
	  install_requires=['requests'],
	  )