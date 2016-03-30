# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

setup(
    name='gdrive-client',
    version='1.0.0.',
    packages=[
        'gdrive',
    ],
    author='Suraj Arya',
    author_email='suraj@loanzen.in',
    description='An simpler lightweight  version of calling google drive apis if you only want to list/upload files',
    url='https://github.com/loanzen/gdrive-client',
    license='MIT',

    install_requires=REQUIRES,
)
