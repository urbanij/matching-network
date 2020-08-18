from setuptools import setup

setup(
    name='matching_network',
    version='0.0.3',
    author='Francesco Urbani',
    author_email='francescourbanidue@gmail.com',
    packages=['matching_network'],
    scripts=[],
    url='https://github.com/urbanij/matching-network',
    license='LICENSE.txt',
    description='Design lumped-parameters matching networks (L-sections)',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "quantiphy==2.10.0",
        "six==1.14.0",
   ],
   keywords="matching networks, lumped parameters, RF electronics",
   python_requires=">=3.7",

)