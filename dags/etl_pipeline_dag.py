from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Import your ETL function
from etl_script import etl_pipeline  # change to your file name

default_args = {
    'owner': 'aryan',
    'depends_on_past': False,
    'start_date': datetime(2025, 8, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'etl_pipeline_dag',
    default_args=default_args,
    description='ETL Pipeline DAG',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    run_etl = PythonOperator(
        task_id='run_etl',
        python_callable=etl_pipeline,
    )

    run_etl
