from prefect import flow, task, get_run_logger

@task
def log_message(name):
    logger = get_run_logger()
    logger.info(f"Hello {name}!")

@flow(name="leonardo_dicaprio_flow")
def leonardo_dicaprio_flow(name:str):
    log_message(name)

leonardo_dicaprio_flow("Leo")
