from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 30),
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
}

with DAG(
    'run_extract_py',
    default_args=default_args,
    schedule_interval=None,  # Run on demand; set cron if needed
    catchup=False,
) as dag:

    run_extract = BashOperator(
        task_id='run_extract_py_script',
        bash_command='python3 /home/airflow/gcs/dags/extract.py',
    )

    run_extract
