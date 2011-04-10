import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
setup(
    name = "fusiontable",
    version = "0.0.1",
    description='Fusion table client',
    packages = find_packages(),
)
