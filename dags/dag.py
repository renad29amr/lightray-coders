# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta
# from airflow.decorators import task
# from airflow.models import Variable

# def add_numbers():
#     num1 = int(Variable.get("number1"))
#     num2 = int(Variable.get("number2"))
#     result = num1 + num2
#     print(f"Result of {num1} + {num2} = {result}")
#     return result

# with DAG(
#     dag_id="second_pip",
#     start_date=datetime(2025, 1, 1),
#     schedule=None,  
#     catchup=False,
# ) as dag:

#     add_task = PythonOperator(
#         task_id="add_numbers_task",
#         python_callable=add_numbers,
#     )


# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime
# from airflow.sdk import Variable 

# def add_numbers():
#     num1 = int(Variable.get("number1", default=0))
#     num2 = int(Variable.get("number2", default=0))
#     result = num1 + num2
#     print(f"Result of {num1} + {num2} = {result}")
#     return result

# with DAG(
#     dag_id="second_pip",
#     start_date=datetime(2025, 1, 1),
#     schedule=None,
#     catchup=False,
# ) as dag:

#     add_task = PythonOperator(
#         task_id="add_numbers_task",
#         python_callable=add_numbers,
#     )




# @task (dag = dag)
# def hello_world(**kwargs):
#     name = kwargs['dag_run'].conf.get('name','no name')
#     print(f'hello world {name}')
    
# def print_message():
#     print("hello task 2:)")
    
# def course_name(course):
#     print(f"Cousrse name ---> {course}")
    
    
# dag  = DAG(
    
# )
# # with DAG(
# #     dag_id = 'first_pipeline',
# #     start_date = datetime(2025,9,27),
# #     schedule = None,
# #     catchup = False,
# #     params = {
# #         'name':'Enter your name: '
# #     }
# # )as dag:
# #     t1 = PythonOperator(
# #         task_id = 'hello_task',
# #         python_callable = hello_world
# #     )
# #     t2 = PythonOperator(
# #         task_id = 'hello2',
# #         python_callable = print_message
# #     )
    
# #     t1 >> t2


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.decorators import task
from airflow.models import Variable


with DAG(
    dag_id="first_pip",
    start_date=datetime(2025, 10, 2),
    schedule=None,  
    catchup=False,
    params = {
        'name' : 'Enter your name: '
    }
) as dag:

    @task (dag = dag)
    def hello_world(**kwargs):
        name = kwargs['dag_run'].conf.get('name','no name') #If none is given, it defaults to (no name)
        print(f'hello world {name}')
        
    @task (dag = dag)
    def print_message():
        print("hello task 2:)")
        
        
    courses = ['java', 'c', 'c++']
    @task(dag=dag)
    def course_name(course):
        print(f"Cousrse name ---> {course}")
        
    t1 = hello_world()
    t2 =print_message()
    t3 = course_name.expand(course=courses)
    
    # Here, python_callable is the function that gets executed.

    # You can also use other operators like:

    # BashOperator → run shell commands

    # EmailOperator → send emails

    # HttpSensor → wait for an API response


    t1 >> t2 >> t3
    
    
with DAG(
    dag_id="add_two_numbers",
    start_date=datetime(2025, 10, 2),
    schedule=None,
    catchup=False,
    params={  
        'a': 0,
        'b': 0
    }
) as dag:

    @task
    def add_numbers(**kwargs):
        a = int(kwargs['dag_run'].conf.get('a' , 0))
        b = int(kwargs['dag_run'].conf.get('b', 0))
        result = a + b
        print(f"Result of {a} + {b} = {result}")
        return result

    add_numbers()
