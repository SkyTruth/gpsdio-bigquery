=====================
gpsdio bigquery schema plugin
=====================


.. image:: https://travis-ci.org/SkyTruth/gpsdio-bigquery-schema.svg?branch=master
    :target: https://travis-ci.org/SkyTruth/gpsdio-bigquery-schema


.. image:: https://coveralls.io/repos/SkyTruth/gpsdio-bigquery-schema/badge.svg?branch=master
    :target: https://coveralls.io/r/SkyTruth/gpsdio-bigquery-schema


A CLI plugin for `gpsdio` that produces a schema file for BigQuery to be used together with CSV output from gpsdio-csv for exporting data into Google's BigQuery.


Examples
--------

See ``gpsdio bq-schema --help`` for info.

.. code-block:: console

    $ gpsdio bq-schema schema.json \
        -c mmsi,timestamp,lat,lon,extra


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
