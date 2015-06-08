"""
Unittests for `gpsdio_bigquery_schema.core`.
"""


import tempfile

from click.testing import CliRunner
import gpsdio.cli
import os
import contextlib
import json
import glob

@contextlib.contextmanager
def unittestfiles():
    try:
        yield
    finally:
        for name in glob.glob("unittest.out.*"):
            os.unlink(name)


def test_bigquery_schema():
    with unittestfiles():
        result = CliRunner().invoke(gpsdio.cli.main.main_group, [
            'bq-schema',
            '-c', 'timestamp,extra',
            'unittest.schema.json'
        ])
        
        with open('unittest.schema.json') as f:
            schema = json.load(f)

        assert len(schema) == 2
        assert schema[0]['name'] == 'timestamp'
        assert schema[0]['type'] == 'TIMESTAMP'
        assert schema[1]['name'] == 'extra'
        assert schema[1]['type'] == 'STRING'
