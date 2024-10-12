Overview
========

  --------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  tests     [![GitHub Actions Build Status](https://github.com/cosgroma/python-file-manager/actions/workflows/github-actions.yml/badge.svg)](https://github.com/cosgroma/python-file-manager/actions) [![Coverage Status](https://codecov.io/gh/cosgroma/python-file-manager/branch/main/graphs/badge.svg?branch=main)](https://app.codecov.io/github/cosgroma/python-file-manager)
  package   [![PyPI Package latest release](https://img.shields.io/pypi/v/sgt-file-manager.svg)](https://pypi.org/project/sgt-file-manager) [![PyPI Wheel](https://img.shields.io/pypi/wheel/sgt-file-manager.svg)](https://pypi.org/project/sgt-file-manager) [![Supported versions](https://img.shields.io/pypi/pyversions/sgt-file-manager.svg)](https://pypi.org/project/sgt-file-manager) [![Supported implementations](https://img.shields.io/pypi/implementation/sgt-file-manager.svg)](https://pypi.org/project/sgt-file-manager) [![Commits since latest release](https://img.shields.io/github/commits-since/cosgroma/python-file-manager/v0.0.0.svg)](https://github.com/cosgroma/python-file-manager/compare/v0.0.0...main)
  --------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

File Management Library

-   Free software: MIT license

Installation
------------

    pip install sgt-file-manager

You can also install the in-development version with:

    pip install https://github.com/cosgroma/python-file-manager/archive/main.zip

Documentation
-------------

To use the project:

``` {.python}
import sgt_file_manager
sgt_file_manager.compute(...)
```

Development
-----------

To run all the tests run:

    tox

Note, to combine the coverage data from all the tox environments run:

+------+---------------------------------------------------------------+
| Win  |     set PYTEST_ADDOPTS=--cov-append                           |
| dows |     tox                                                       |
+------+---------------------------------------------------------------+
| O    |     PYTEST_ADDOPTS=--cov-append tox                           |
| ther |                                                               |
+------+---------------------------------------------------------------+
