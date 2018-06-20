#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

py_modules = [
    'tickettools',
    'scripts/create_bulk_ticket_with_template'
]

requires = ['python-rtkit',  'sphinxapi-py3', 'defang', 'click']

with open('README.rst', 'r') as f:
    readme = f.read()
#with open('CHANGELOG.md', 'r') as f:
    #changelog = f.read()

setup(
    name='tickettools',
    version='0.0.1',
    author='Sascha Rommelfangen ',
    author_email=' sascha@rommelfangen.de',
    url='https://github.com/rommelfs/ticket-tools',
    description='ticket tools.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    #scripts=scripts,
    #py_modules=py_modules,
    entry_points='''
        [console_scripts]
        ticket-tools=tickettools:main
        ticket-tools-avalanche=scripts.create_bulk_ticket_with_template:main
    ''',
    platforms = ['Linux'],
    license='GPLv3',
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Security',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
    ]
)
