from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def print_rows():
    pg_hook = PostgresHook(postgres_conn_id='postgres_db')
    
    sql_query = """
    SELECT v.id, c.marca, c.modelo, cl.nome AS cliente_nome, f.nome AS funcionario_nome, v.data_da_venda, v.preco_de_venda
    FROM vendas v
    JOIN carros c ON v.carro_id = c.id
    JOIN clientes cl ON v.cliente_id = cl.id
    JOIN funcionarios f ON v.funcionario_id = f.id;
    """
    conn = pg_hook.get_conn()
    cursor = conn.cursor()
    cursor.execute(sql_query)
    
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

with DAG('print_rows_dag', default_args=default_args, schedule_interval=None) as dag:

    print_rows_task = PythonOperator(
        task_id='print_rows_task',
        python_callable=print_rows
    )

    print_rows_task