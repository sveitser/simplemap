"""Simplemap"""
from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='simplemap',
    version='0.0.1',
    description='Plot GPS coordinates',
    long_description=long_description,
    url='https://github.com/patrick--/simplemap',
    author='Patrick Servello',
    license='MIT',
    keywords='google maps geo',
    packages=['simplemap'],
    include_package_data=True,
    #data_files=[('simplemap/templates/static/css', ['simplemap/templates/static/css/basic.css']),
    #            ('simplemap/templates', ['simplemap/templates/basic.html'])],
    install_requires=['Jinja2'],
)
