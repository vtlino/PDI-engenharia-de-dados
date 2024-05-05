from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define the Python function to print "Hello, World!"
def print_hello():
    print("Hello, World!")

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retry': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG('hello_world',
         default_args=default_args,
         description='A simple DAG to print Hello, World! with null schedule',
         schedule_interval=None) as dag:

    # Create a task to print "Hello, World!"
    print_hello_task = PythonOperator(
        task_id='print_hello_task',
        python_callable=print_hello,
    )