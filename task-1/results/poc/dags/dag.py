from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime
import pandas as pd

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

def read_csv():
    df = pd.read_csv('/opt/airflow/data/input.csv')
    df.to_pickle('/opt/airflow/data/data.pkl')

def transform():
    df = pd.read_pickle('/opt/airflow/data/data.pkl')
    df['transformed_col'] = df.iloc[:, 0] * 2
    df.to_pickle('/opt/airflow/data/data.pkl')

def choose_branch():
    df = pd.read_pickle('/opt/airflow/data/data.pkl')
    if df.iloc[:, 0].sum() > 100:
        return 'job1'
    else:
        return 'job2'

def job1():
    df = pd.read_pickle('/opt/airflow/data/data.pkl')
    df['result'] = df['transformed_col'] + 1
    df.to_csv('/opt/airflow/data/result.csv', index=False)

def job2():
    df = pd.read_pickle('/opt/airflow/data/data.pkl')
    df['result'] = df['transformed_col'] - 1
    df.to_csv('/opt/airflow/data/result.csv', index=False)

dag = DAG('csv_processing', default_args=default_args, schedule=None, catchup=False)
read_task = PythonOperator(task_id='read_csv', python_callable=read_csv, dag=dag)
transform_task = PythonOperator(task_id='transform', python_callable=transform, dag=dag)
branch_task = BranchPythonOperator(task_id='branching', python_callable=choose_branch, dag=dag)
job1_task = PythonOperator(task_id='job1', python_callable=job1, dag=dag)
job2_task = PythonOperator(task_id='job2', python_callable=job2, dag=dag)

read_task >> transform_task >> branch_task
branch_task >> [job1_task, job2_task]
# (job1_task >> job2_task) or (job2_task >> job1_task)

