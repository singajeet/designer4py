""" Setup.py file for bipy package
"""
from setuptools import setup

setup(
    name="designer4py",
    version="0.1.0",
    author="Ajeet Singh",
    author_email="singajeet@gmail.com",
    packages=["designer4py"],
    url="https://github.com/singajeet/designer4py",
    license="LICENSE.txt",
    description="HTML based designer to be used in python app",
    long_description=open('README.txt').read(),
    install_requires=["Config"]
)
