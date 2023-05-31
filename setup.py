from setuptools import setup

with open('README.md', 'r') as readme_file:
    long_description: str = readme_file.read()

setup(
    name='graph_library',
    version='0.0.1',
    description='Python module for graph processing',
    long_description=long_description,
    include_package_data=True
)
