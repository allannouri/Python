import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

connection_string = "Driver={SQL Server}; Server=XX; Database=XX; Trusted_Connection=yes"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)

out = pd.read_sql("select * from db.schema.table", engine)
exp = pd.read_sql_query("insert into db.schema.table values (X)", engine)

