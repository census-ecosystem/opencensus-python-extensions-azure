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

from setuptools import find_packages, setup

from opencensus_python_extensions_azure import __version__

setup(
    name='opencensus-python-extensions-azure',
    version=__version__,  # noqa
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
    description='OpenCensus Extension for Azure',
    include_package_data=True,
    long_description=open('README.md').read(),
    install_requires=[
        'azure-functions >= 1.7.0',
        'opencensus >= 0.7.12, < 1.0.0'
    ],
    extras_require={},
    license='Apache-2.0',
    packages=find_packages(exclude=('examples', 'tests',)),
    namespace_packages=[],
    url='https://github.com/census-ecosystem/opencensus-python-extensions-azure',  # noqa: E501
    zip_safe=False,
)
