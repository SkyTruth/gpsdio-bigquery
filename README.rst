=====================
gpsdio sorting plugin
=====================


.. image:: https://travis-ci.org/SkyTruth/gpsdio-bigquery.svg?branch=master
    :target: https://travis-ci.org/SkyTruth/gpsdio-bigquery


.. image:: https://coveralls.io/repos/SkyTruth/gpsdio-bigquery/badge.svg?branch=master
    :target: https://coveralls.io/r/SkyTruth/gpsdio-bigquery


A CLI plugin for `gpsdio <https://github.com/skytruth/gpdsio/>`_ that sorts messages in arbitrarily large files according to an arbitrary set of columns.


Examples
--------

See ``gpsdio sort --help`` for info.

.. code-block:: console

    $ gpsdio sort input.msg output.msg \
        -c mmsi,timestamp


Installing
----------

Via pip:

.. code-block:: console

    $ pip install gpsdio-bigquery

From master:

.. code-block:: console

    $ git clone https://github.com/SkyTruth/gpsdio-bigquery
    $ cd gpsdio-bigquery
    $ pip install .


Developing
----------

.. code-block::

    $ git clone https://github.com/SkyTruth/gpsdio-bigquery
    $ cd gpsdio-bigquery
    $ virtualenv venv && source venv/bin/activate
    $ pip install -e .[test]
    $ py.test tests --cov gpsdio_bigquery --cov-report term-missing
