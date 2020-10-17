#!/usr/bin/env python3

import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='opensusbot',
    version='1.0.0',
    description='Discord bot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='OpenSuspect community',
    url='https://github.com/OpenSuspect/OpenSusBot',
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': [
        'opensusbot = opensusbot.__main__:main'
    ]}
)
