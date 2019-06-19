from setuptools import setup, find_packages

setup(
 name='CrossFit Games Leaderboard API',
 version='1.0',
 author='Tony Silva',
 author_email='tonysilva.ou@gmail.com',
 packages=find_packages(exclude=('tests', 'docs', 'analysis', 'sample_data_scripts')),
 setup_requires=['pytest-runner'],
 tests_require=['pytest'],
)