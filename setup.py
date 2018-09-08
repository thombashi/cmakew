# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

import os.path
import sys

import setuptools


REQUIREMENT_DIR = "requirements"


with open("README.rst") as fp:
    long_description = fp.read()

with open(os.path.join("docs", "pages", "introduction", "summary.txt")) as f:
    summary = f.read()

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

MODULE_NAME = "cmakew"
needs_pytest = set(["pytest", "test", "ptr"]).intersection(sys.argv)
pytest_runner = ["pytest-runner"] if needs_pytest else []

setuptools.setup(
    name=MODULE_NAME,
    version="0.0.6",
    url="https://github.com/thombashi/{:s}".format(MODULE_NAME),

    author="Tsuyoshi Hombashi",
    author_email="tsuyoshi.hombashi@gmail.com",
    description=summary,
    include_package_data=True,
    keywords=["cmake", "build", "Visual Studio"],
    license="MIT License",
    long_description=long_description,
    packages=setuptools.find_packages(exclude=['test*']),
    project_urls={
        "Tracker": "{:s}/issues".format(REPOSITORY_URL),
    },

    install_requires=install_requires,
    setup_requires=pytest_runner,
    tests_require=[],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*',
    extras_require={
        "build": "wheel",
        "release": "releasecmd>=0.0.12",
    },

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Build Tools",
    ],
    entry_points={
        "console_scripts": [
            "cmakew=cmakew.cmakew:main",
        ],
    }
)
