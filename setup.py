#!/usr/bin/env python

from setuptools import setup

setup(
    name='kasa_automation',
    version='0.01',
    description='Automating Kasa smart bulbs',
    author='n_sweep',
    author_email='n@sweep.sh',
    packages=['kasa_automation'],
    install_requires=[  # external package dependencies
        'kasa',
        'python-crontab',
        'requests'
    ],
)
