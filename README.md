# ddl helper

How to read DDL and create XLS representations of a schema.

This can be extended in cases where your DDL is not in one file but in multiple, by applying your sequenced
DDL against sqlite3 and then exporting the final schema, parsing it and then preparing the xls output.