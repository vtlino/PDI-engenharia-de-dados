from airflow import DAG 
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta

args = {
    'owner': 'sales',
    'email_on_retry': None,
    'email_on_failure': None,
    'retry': 2,
    'retry_delay': timedelta(minutes=5)
}

def print_ds(ti, ds):
    ti.xcom_push(key='ds', value=ds)
    print("O valor de ds é:", ds)

def print_ts(ti, ts):
    ti.xcom_push(key='ts', value=ts)
    print("O valor de ts é:", ts)

def print_final(ti):
    ds=ti.xcom_pull(key="ds")
    ts=ti.xcom_pull(key="ts")
    print("O resultado final é:")
    print(f"<{ds}> -- <{ts}>")

with DAG (
    dag_id="tp4-2",
    schedule_interval=None,
    catchup=True,
    start_date=datetime(2024,5,1),
    default_args = args,
    tags=["multitask"]

) as dag:

    bash_operator_task=BashOperator(
        task_id='bash_operator_task',
        bash_command='echo "A dag foi iniciada"',
        dag=dag
    )

    print_ds_task = PythonOperator(
        task_id='print_ds_task',
        python_callable=print_ds,
        provide_context=True,
        dag=dag
    )

    print_ts_task = PythonOperator(
        task_id='print_ts_task',
        python_callable=print_ts,
        provide_context=True,
        dag=dag
    )

    dummy_task = DummyOperator(
        task_id='dummy_task',
        dag=dag
    )

    print_final_task = PythonOperator(
        task_id='print_final_task',
        python_callable=print_final,
        provide_context=True,
        dag=dag
    )

    bash_operator_task >> [print_ds_task, print_ts_task] >> dummy_task >> print_final_task