#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(name='finedr',
      version='1.0',
      packages=find_packages(),
      install_requires=[
        'Django==2.2.13',
        'django-cors-headers==2.4.0',
        'django-extra-fields==1.0.0',
        'djangorestframework==3.9.1',
        'Pillow==5.4.1',
        'pytz==2018.9'
      ],
      scripts=['./manage.py'])
