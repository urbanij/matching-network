========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/matching-network/badge/?style=flat
    :target: https://readthedocs.org/projects/matching-network
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/urbanij/matching-network.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/urbanij/matching-network

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/urbanij/matching-network?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/urbanij/matching-network

.. |requires| image:: https://requires.io/github/urbanij/matching-network/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/urbanij/matching-network/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/urbanij/matching-network/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/urbanij/matching-network

.. |version| image:: https://img.shields.io/pypi/v/matching-network.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/matching-network

.. |wheel| image:: https://img.shields.io/pypi/wheel/matching-network.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/matching-network

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/matching-network.svg
    :alt: Supported versions
    :target: https://pypi.org/project/matching-network

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/matching-network.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/matching-network

.. |commits-since| image:: https://img.shields.io/github/commits-since/urbanij/matching-network/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/urbanij/matching-network/compare/v0.0.0...master



.. end-badges

Design matching network (L-sections)

Installation
============

::

    pip install matching-network

You can also install the in-development version with::

    pip install https://github.com/urbanij/matching-network/archive/master.zip


Documentation
=============


https://matching-network.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
