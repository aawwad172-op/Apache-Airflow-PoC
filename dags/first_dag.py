import datetime
from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator


# Each Dag represent a workflow (a collection of tasks)
with DAG(
    dag_id="first_dag",
    start_date=datetime.datetime(2024, 12, 30),
    schedule="06 8 * * *",
    is_paused_upon_creation=False,
) as dag:

    # Each task represented as operators
    hello = BashOperator(task_id="hello", bash_command='echo "Hello"')

    # Another task represented as a function
    @task()
    def airflow():
        print("Airflow")

    # Task dependencies
    hello >> airflow()
