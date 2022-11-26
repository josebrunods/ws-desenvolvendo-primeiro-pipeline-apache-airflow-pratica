
# import libraries
import os
from datetime import date, datetime, timedelta

from airflow.decorators import dag
from airflow.operators.dummy import DummyOperator

from astro import sql as aql
from astro.constants import FileType
from astro.files import File
from astro.table import Metadata, Table
import pathlib

from datetime import datetime
import pandas as pd


# connections

#S3_FILE_PATH_BUSINESS = "s3://landing-workshop/business/yelp_academic_dataset_business_2018.json"
S3_FILE_PATH_USERS = "s3://landing-workshop/user/users_2022_10_11_16_8_16.json"
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
    
    
    #business = aql.load_file(
    #   task_id = "business", 
    #   input_file=File(path=S3_FILE_PATH_BUSINESS,conn_id=AWS_CONN_ID,filetype=FileType.NDJSON))
    
    user = aql.load_file(
       task_id = "user", 
       input_file=File(path=S3_FILE_PATH_USERS,conn_id=AWS_CONN_ID,filetype=FileType.JSON))
    
    



    # finish
    finish = DummyOperator(task_id="finish")

    # define sequence
    init >> user >> finish


# init dag
dag = ingest_data()