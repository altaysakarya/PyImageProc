from setuptools import setup, find_packages

setup(
    name='pyimageproc',
    version='0.1',
    description='A simple image processing library',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
)
