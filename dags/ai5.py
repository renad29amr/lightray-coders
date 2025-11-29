# from datetime import datetime, timedelta
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# import sys
# import os
# from airflow.operators.bash import BashOperator
# from airflow.operators.email import EmailOperator
# sys.path.append(os.path.dirname(__file__))

# from s5.data_loader import load_data

# with DAG(
#     dag_id = 'data_pipeline',
#     description='LOAD DATA FROM API --> TRANSFORM DATA ',
#     schedule = None,
#     catchup = False, 
#     tags = ['email'],
#     start_date = datetime(2025,10,4),
#     default_args = {
#         'retries':2,
#         'retry_delay' : timedelta(minutes=2)
#     }
# ) as dag:

#     t1 = PythonOperator(
#         task_id='load_data_from_api',
#         python_callable=load_data
#     )

#     t2 = BashOperator(
#         task_id='dbt_run',
#         cwd = "/home/renad/airflow/dags/s5",
#         bash_command = "/home/renad/venvs/airflow_3.0.6/bin/dbt run"
#     )
    
#     t3 = EmailOperator(
#     task_id='send_email',
#     to='renadamr.bls@gmail.com',
#     subject='Airflow DAG data_pipeline completed',
#     html_content="<h3>Data pipeline finished successfully 🎉</h3>"
#     )


    
#     t1>>t2>>t3

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import smtplib, ssl
import sys
import os

sys.path.append(os.path.dirname(__file__))
from s5.data_loader import load_data

def send_email():
    sender = "renadamr.bls@gmail.com"
    receiver = "renadamr.bls@gmail.com"
    password = "kcfnmppinsniimtc"
    message = f"Subject: data_pipeline completed \n\n data pipeline finished successfully "

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("Email sent successfully:) ")

with DAG(
    dag_id='data_pipeline',
    description='LOAD DATA FROM API --> TRANSFORM DATA',
    schedule=None,
    catchup=False,
    tags=['email'],
    start_date=datetime(2025, 10, 11),
    default_args={
        'retries': 2,
        'retry_delay': timedelta(minutes=2)
    }
) as dag:

    t1 = PythonOperator(
        task_id='load_data_from_api',
        python_callable=load_data
    )

    t2 = BashOperator(
        task_id='dbt_run',
        cwd="/home/renad/airflow/dags/s5",
        bash_command="/home/renad/venvs/airflow_3.0.6/bin/dbt run"
    )

    t3 = PythonOperator(
        task_id='send_email',
        python_callable=send_email
    )
    
    t1 >> t2 >> t3


