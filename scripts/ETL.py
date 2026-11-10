import pandas as pd
import sqlite3
import logging
from ingestion import ingest_data


conn = sqlite3.connect('../inventory.db')

#set up different log file for country analysis
logger = logging.getLogger('country_analysis')
logger.setLevel(logging.INFO)
logger.propagate = False
file_handler = logging.FileHandler('logs/country_analysis.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
if not logger.handlers:
    logger.addHandler(file_handler)

#creating a function to create country analysis dataframe
def create_country_analysis(conn):
    query = """WITH country1 AS (SELECT
                                                         [country],
                                                         [Exports of goods and services (% of GDP)],
                                                         [Purchasing Power Index],
                                                         [Safety Index],
                                                         [Health Care Index],
                                                         [Cost Of Living Index],
                                                         [Access to electricity (% of population)],
                                                         [Education: Government expenditure (% of GDP)],
                                                         [Quality Of Life Index]
                                                         FROM [country economy] SC
                                                         WHERE [Exports of goods and services (% of GDP)]>="18.7826851657717"
                                                         ORDER BY [Exports of goods and services (% of GDP)]
                                   ),
                                   country2 AS (SELECT
                                                 [govt_type],
                                                 [country_name]
                                                 FROM [country_govt_type] AV
                                   )
                                    SELECT
                                                    SC.[country],
                                                    SC.[Exports of goods and services (% of GDP)],
                                                    SC.[Purchasing Power Index],
                                                    SC.[Safety Index],
                                                    SC.[Health Care Index],
                                                    SC.[Cost Of Living Index],
                                                    SC.[Access to electricity (% of population)],
                                                    SC.[Education: Government expenditure (% of GDP)],
                                                    SC.[Quality Of Life Index],
                                                    AV.[govt_type]
                                    FROM country1 SC
                                    LEFT JOIN country2 AV
                                      ON SC.[country] = AV.[country_name]
                                    ORDER BY SC.[Exports of goods and services (% of GDP)]
"""
    return pd.read_sql_query(query, conn)


def clean_data(df):
    df=df.rename(columns={'Education: Government expenditure (% of GDP)': 'Government expenditure on education (% of GDP)'})
    df['Government expenditure on education (% of GDP)'] = pd.to_numeric(df['Government expenditure on education (% of GDP)'], errors='coerce').replace(-99,pd.NA)
    mean_value = df['Government expenditure on education (% of GDP)'].mean()
    df['Government expenditure on education (% of GDP)'] = df['Government expenditure on education (% of GDP)'].fillna(mean_value).replace(0, mean_value)
    return df


if __name__ == "__main__":
    conn = sqlite3.connect('inventory.db')

    logger.info("-----creating_country_analysis-----")
    country_analysis_df = create_country_analysis(conn)
    logger.info(country_analysis_df.head())

    logger.info("---cleaning data---")
    clean_df = clean_data(country_analysis_df)
    logger.info(clean_df.head())

    logger.info("---ingesting data---")
    ingest_data(clean_df, "country_analysis", conn)
    logger.info("---------completed------------------")   