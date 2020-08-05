from setuptools import setup

setup(
    name='matching_network',
    version='0.0.1',
    author='Francesco Urbani',
    author_email='francescourbanidue@gmail.com',
    packages=['matching_network'],
    scripts=[],
    url='http://pypi.python.org/pypi/matching_network/',
    license='LICENSE.txt',
    description='Design matching network (L-sections)',
    long_description=open('README.rst').read(),
    install_requires=[
        "quantiphy==2.10.0",
        "six==1.14.0",
   ],
)