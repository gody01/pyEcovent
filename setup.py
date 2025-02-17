# coding=utf8
from setuptools import setup

long_description = None

with open("README.md", 'r') as fp:
    long_description = fp.read()

setup(
    name = 'pyecoventv2',
    packages = ['ecovent','ecoventv2'],
    version='0.9.22',
    description='Python3 library for single-room energy recovery ventilators from Vents / Blauberg / Flexit',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6.7',
    author='Aleksander Lehmann',
    author_email='aleksander@flovik.no',
    maintainer='Matjaž Godec',
    maintainer_email = 'matjaz.godec@gmail.com',
    url='https://github.com/gody0/pyEcoventV2',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)
