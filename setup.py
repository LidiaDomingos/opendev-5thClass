#!/usr/bin/env python3
from setuptools import setup

setup(name='dev_aberto_lidiaacd',
      version='0.1',
      packages=['dev_aberto'],
      author="LidiaDomingos",
      install_requires=['requests',],
      scripts=['scripts/hello.py']  
      )