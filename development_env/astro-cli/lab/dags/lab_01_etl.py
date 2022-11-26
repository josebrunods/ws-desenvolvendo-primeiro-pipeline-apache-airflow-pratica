
# import libraries
import os
from datetime import date, datetime, timedelta

from airflow.decorators import dag
from airflow.operators.dummy import DummyOperator

from astro import sql as aql
from astro.constants import FileType
from astro.files import File

import pathlib

from datetime import datetime
import pandas as pd


# connections

S3_FILE_PATH_BUSINESS = "s3://landing-workshop/business/yelp_academic_dataset_business_2018.json"
OUTPUT_FILE_PATH_BUSINESS = "s3://landing-workshop/business"
AWS_CONN_ID = "aws_default"


# default args & init dag
current_date = date.today()
get_year = current_date.year
get_month = current_date.month
get_day = current_date.day



CWD = pathlib.Path(__file__).parent
default_args = {
    "owner": "Mateus Oliveira",
    "retries": 1,
    "retry_delay": 0
}


# declare dag
@dag(
    dag_id="extract-s3-json-files",
    start_date=datetime(2022, 11, 22),
    max_active_runs=1,
    schedule_interval=timedelta(hours=24),
    default_args=default_args,
    catchup=False,
    tags=['development', 'ingestion', 's3']
)
# init main function
def ingest_data():

    # set tasks

    # init
    init = DummyOperator(task_id="init")
    
    
    business = aql.load_file(
       task_id = "business", 
       input_file=File(path=S3_FILE_PATH_BUSINESS,conn_id=AWS_CONN_ID,filetype=FileType.NDJSON))
    
   
    @aql.dataframe(columns_names_capitalization="original")
    def extract_top_5_business(input_df: pd.DataFrame):
        print(f"Total Number of records: {len(input_df)}")
        top_5_business = input_df.sort_values(by="review_count", ascending=False)[["review_count", "name", "city"]].head(
            5
        )
        print(f"Top 5 business: {top_5_business}")
        return top_5_business


    
        
    # Running transformation using dataframe
    transf_df = extract_top_5_business(input_df=business)
    
    
    
    # create export json
    save_json_to_minio = aql.export_file(
        task_id="save_json_to_minio",
        input_data=transf_df,
        output_file=File(
            path=f"{OUTPUT_FILE_PATH_BUSINESS}/output_business.json",
            conn_id=AWS_CONN_ID,
        ),
        if_exists="replace",
    )
    
    save_parquet_to_minio = aql.export_file(
        task_id="save_parquet_to_minio",
        input_data=transf_df,
        output_file=File(
            path=f"{OUTPUT_FILE_PATH_BUSINESS}/output_business.parquet",
            conn_id=AWS_CONN_ID,
        ),
        if_exists="replace",
    )
          

    # finish
    finish = DummyOperator(task_id="finish")

    # define sequence
    init >> business >> save_json_to_minio >> save_parquet_to_minio >> finish


# init dag
dag = ingest_data()