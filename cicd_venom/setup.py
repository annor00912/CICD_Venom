from setuptools import setup, find_packages

setup(name='cicd-venom',version='1.0.0',packages=find_packages(),entry_points={'console_scripts':['cicdvenom=cicdvenom.main:main']},install_requires=['requests','rich'])