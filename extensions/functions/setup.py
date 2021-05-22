# Copyright 2019, OpenCensus Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from setuptools import find_namespace_packages, setup

BASE_DIR = os.path.dirname(__file__)
VERSION_FILENAME = os.path.join(BASE_DIR, "src", "opencensus", "azure", "functions", "version.py")
PACKAGE_INFO = {}
with open(VERSION_FILENAME) as f:
    exec(f.read(), PACKAGE_INFO)

setup(
    name='opencensus-extensions-azure-functions',
    version=PACKAGE_INFO["__version__"],
    author='OpenCensus Azure',
    author_email='opencensusazure@microsoft.com',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='OpenCensus extension for Azure Functions',
    include_package_data=True,
    long_description=open('README.rst').read(),
    install_requires=[
        'azure-functions >= 1.7.0, < 2.0.0',
        'opencensus-ext-azure >= 1.0.4, < 2.0.0'
    ],
    extras_require={},
    license='Apache-2.0',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    url='https://github.com/census-ecosystem/opencensus-python-extensions-azure',
    zip_safe=False,
)
