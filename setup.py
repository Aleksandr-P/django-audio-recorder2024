from setuptools import setup, find_packages
import os
import sys

__version__ = '0.0.1'
__requirements__ = [

]

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

setup(
    name='django-audio-recorder2024',
    version=__version__,
    packages=find_packages('audio_recorder'),
    install_requires=__requirements__,
)
