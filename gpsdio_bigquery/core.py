#!/usr/bin/env python


"""
Core components for gpsdio_bigquery
"""


import click
import gpsdio
import gpsdio.schema
import datetime
import json


typemap = {
    str: "STRING",
    unicode: "STRING",
    float: "FLOAT",
    int: "INTEGER",
    datetime.datetime: "TIMESTAMP"
}

def type_for_col(col):
    if col == 'extra' or col not in gpsdio.schema.CURRENT or gpsdio.schema.CURRENT[col]['type'] not in typemap:
        return 'STRING'
    return typemap[gpsdio.schema.CURRENT[col]['type']]

default_cols = ["type", "mmsi", "timestamp", "lon", "lat", "heading", "turn", "course", "speed", "extra"]



@click.command(name='bigquery-schema')
@click.option(
    '-c', '--cols', metavar='COL,[COL,...]', default=','.join(default_cols),
    help="Columns to export to BigQuery. Default: " + ','.join(default_cols),
)
@click.argument("schemafile")
@click.pass_context
def gpsdio_bigquery(ctx, schemafile, cols):
    """
    Produce a BigQuery schema for a set of GPSD columns, suitable for
    use together with CSV output from gpsdio-csv.
    """

    cols = cols.split(",")

    schema = [{"type": type_for_col(col), "name": col}
              for col in cols]

    with open(schemafile, "w") as f:
        json.dump(schema, f)


if __name__ == '__main__':
    gpsdio_bigquery()
