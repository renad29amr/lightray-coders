import requests
import pandas as pd
import duckdb
import os

def load_data ():
    url = "https://api.escuelajs.co/api/v1/products"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError('Failed to call api')
    data = response.json()
    
    data = pd.json_normalize(data)

    db_path = os.path.join(os.path.dirname(__file__), 'dev.duckdb')
    conn = duckdb.connect(db_path)
    conn.sql('create table if not exists raw_products as select * from data')

    conn.close()