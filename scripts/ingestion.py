import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
    )

engine = create_engine('sqlite:///inventory.db')

def ingest_data(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_raw_data():
    start_time = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/'+file)
            logging.info(f'Ingesting {file} into database')
            ingest_data(df, file[:-4], engine)
    end_time = time.time()
    total_time = (end_time - start_time)/60
    logging.info('--------Finished ingesting-------')
    logging.info(f'\nTotal time taken: {total_time} minutes')

if __name__ == "__main__":
    load_raw_data()