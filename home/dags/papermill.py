import airflow

from airflow.models import DAG
#from airflow.operators.papermill_operator import PapermillOperator
from airflow.operators.bash_operator import BashOperator

from datetime import timedelta

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2)
}

dag = DAG(
    dag_id='papermill', default_args=args,
    schedule_interval='*/5 * * * *',
    dagrun_timeout=timedelta(minutes=60))

templated_command = """
    papermill \
    /home/lukas/work/test/airflow/notebooks/test_parametrization.ipynb \
    /home/lukas/work/test/airflow/out/test_parametrization/test_parametrization-{{ execution_date }}.ipynb \
    -p timestamp {{ execution_date }} \
    -p msg "Run from airflow on {{ execution_date }}"
"""

run_ntb = BashOperator(
    task_id='run_ntb',
    depends_on_past=False,
    bash_command=templated_command,
    dag=dag)

#run_this = PapermillOperator(
#    task_id="run_example_notebook",
#    dag=dag,
#    input_nb="/tmp/hello_world.ipynb",
#    output_nb="/tmp/out-{{ execution_date }}.ipynb",
#    parameters={"msgs": "Ran from Airflow at {{ execution_date }}!"}
#)
