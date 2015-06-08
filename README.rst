=====================
gpsdio sorting plugin
=====================


.. image:: https://travis-ci.org/SkyTruth/gpsdio-bigquery-schema.svg?branch=master
    :target: https://travis-ci.org/SkyTruth/gpsdio-bigquery-schema


.. image:: https://coveralls.io/repos/SkyTruth/gpsdio-bigquery-schema/badge.svg?branch=master
    :target: https://coveralls.io/r/SkyTruth/gpsdio-bigquery-schema


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

    $ pip install gpsdio-bigquery-schema

From master:

.. code-block:: console

    $ git clone https://github.com/SkyTruth/gpsdio-bigquery-schema
    $ cd gpsdio-bigquery-schema
    $ pip install .


Developing
----------

.. code-block::

    $ git clone https://github.com/SkyTruth/gpsdio-bigquery-schema
    $ cd gpsdio-bigquery-schema
    $ virtualenv venv && source venv/bin/activate
    $ pip install -e .[test]
    $ py.test tests --cov gpsdio_bigquery_schema --cov-report term-missing
