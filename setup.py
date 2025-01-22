from setuptools import setup, find_packages

setup(
    name='cta_custom_objects',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'stix2'
        ]
)
