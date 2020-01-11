from setuptools import setup

setup(
    name='temper',
    version='1.0',
    description='Simple library for accessing TEMPer USB thermometers',
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
)
