#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Tony Tung",
    author_email='ttung@chanzuckerberg.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Flattens SpaceTx-formatted datasets to be compatible with the HCA ingest limitations",
    entry_points={
        'console_scripts': [
            'spacetx_hca_flattener=spacetx_hca_flattener.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='spacetx_hca_flattener',
    name='spacetx_hca_flattener',
    packages=find_packages(include=['spacetx_hca_flattener']),
    setup_requires=setup_requirements,
    test_suite='spacetx_hca_flattener',
    tests_require=test_requirements,
    url='https://github.com/ttung/spacetx_hca_flattener',
    version='0.0.0',
    zip_safe=False,
)
