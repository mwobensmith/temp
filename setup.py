# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, find_packages

PACKAGE_NAME = 'temp'
PACKAGE_VERSION = '1.0'

INSTALL_REQUIRES = [
]

TESTS_REQUIRE = [
]

DEV_REQUIRES = [
]

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='Test',
    classifiers=[
        'Topic :: Software Development :: Testing'
    ],
    keywords=['mozilla', 'testing'],
    author='Mozilla',
    author_email='mwobensmith@mozilla.com',
    url='https://github.com/mwobensmith/temp',
    download_url='https://github.com/mwobensmith/temp/latest.tar.gz',
    license='MPL2',
    packages=find_packages(),
    include_package_data=True,  # See MANIFEST.in
    zip_safe=False,
    use_2to3=False,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require={'dev': DEV_REQUIRES},  # For `pip install -e .[dev]`
    entry_points={
    }
)
