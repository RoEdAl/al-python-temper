from os import path
from setuptools import setup

own_dir = path.dirname(path.realpath(__file__))
with open(path.join(own_dir, 'README.md')) as f:
    long_description = f.read()

setup(
    name='temper',
    version='1.0',
    platforms=['posix'],
    description='Simple library for accessing TEMPer USB thermometers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Pham Urwen',
    author_email='urwen@mail.ru',
    maintainer='Edmunt Pienkowsky',
    maintainer_email='roed@onet.eu',
    url='https://github.com/urwen/temper',
    license='MIT',
    packages=['temper'],
    entry_points={
        'console_scripts': [
		'temper=temper.command_line:main'
	]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
)
