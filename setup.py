"""
setup.py

PEP 621 switches most of Packaging to `pyproject.toml` -- yet keep a "dummy" setup.py for external code that has not
yet upgraded.
"""
from setuptools import setup, find_packages

setup(
  name="voltron", 
  packages=find_packages(
    where='.', 
    exclude=['cache'],
  ), 
  package_dir={"": "."},
)
