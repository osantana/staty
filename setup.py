# Copyright 2016 Osvaldo Santana Neto <staty@osantana.me>
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
import re

from setuptools import setup, Command

here = os.path.abspath(os.path.dirname(__file__))

version = "0.0.0"
with open(os.path.join(here, "CHANGES.rst")) as changes:
    for line in changes:
        version = line.strip()
        if re.search('^[0-9]+\.[0-9]+(\.[0-9]+)?$', version):
            break


class VersionCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(version)


setup(
    name='staty',
    version=version,
    description='HTTP response and status code handling',
    author="Osvaldo Santana Neto", author_email="staty@osantana.me",
    license="MIT",
    packages=['staty'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
    ],
    url='http://github.com/osantana/staty',
    download_url='https://github.com/osantana/staty/tarball/{}'.format(version),
    cmdclass={'version': VersionCommand},
    test_suite="tests",
    extras_require={
        'requests': ["requests"],
    },
)
