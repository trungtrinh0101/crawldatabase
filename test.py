import uvicorn
from fastapi import FastAPI
import mysql.connector
import pandas as pd
import pyodbc as odbc
import json
import requests

app = FastAPI()

def fetch_data(connection):

    query = 'SELECT * FROM databds'
    cursor = connection.cursor()
    results = cursor.execute(query).fetchall()
    print(results)

    return results

@app.get("/")
def get_data():
    print('BEGIN')
    connection = mysql.connector.connect(host='localhost',
                                         database='batdongsandn',
                                         user='root',
                                         password='')
    print('BEGIN')

    query = 'SELECT * FROM databds'

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM databds")

    rows = cursor.fetchall()
    print(rows)

    return rows


if __name__ == "__test__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


