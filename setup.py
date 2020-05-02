from setuptools import setup, find_packages

setup(
 name='crossfitgamesleaderboard',
 version='1.0',
 author='Tony Silva',
 author_email='tonysilva.ou@gmail.com',
 packages=find_packages(exclude=('tests', 'docs', 'analysis', 'sample_data_scripts'))
)