from setuptools import setup

setup(
    name='sshmagic',
    version='0.1.0',    
    description='IPython magic for executing commands on a remote machine via ssh',
    url='https://github.com/rwuthric/SSHMagic',
    author='Rolf Wuthrich',
    author_email='rolf.wuthrich@concordia.ca',
    license='BSD 3-Clause License',
    packages=['sshmagic'],
    install_requires=['ipython'],
)