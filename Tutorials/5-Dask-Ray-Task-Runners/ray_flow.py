from prefect import flow, task
from prefect.task_runners import RayTaskRunner

@task
def say_hello(name):
    print("hello", name)

@task
def say_goodbye(name):
    print("Goodbye", name)

@flow(task_runner=RayTaskRunner())
def greetings(names):
    for name in names:
        say_hello(name)
        say_goodbye(name)

if __name__ == "__main__":
    greetings(["arthur", "trillian", "ford", "marvin"])
