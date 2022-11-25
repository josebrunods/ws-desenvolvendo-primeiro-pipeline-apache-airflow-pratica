
# import libraries
import os
from datetime import date, datetime, timedelta

from airflow.decorators import dag
from airflow.operators.dummy import DummyOperator


# default args & init dag
current_date = date.today()
get_year = current_date.year
get_month = current_date.month
get_day = current_date.day

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

   

    # finish
    finish = DummyOperator(task_id="finish")

    # define sequence
    init >> finish


# init dag
dag = ingest_data()