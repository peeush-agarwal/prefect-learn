# prefect-learn

Prefect (Model orchestration tool) learning resources.

[Reference](https://orion-docs.prefect.io/tutorials)

## Get started

1. Create conda virtual environment: `conda env create -f requirements.yaml`
1. Activate the conda environment: `conda activate prefect-env`
1. Good to go!

## Tutorials

1. [First steps](Tutorials/1-First-Steps/first_steps.ipynb)
1. [Flow and Task Configuration](Tutorials/2-Flow-And-Task-Configuration/flow_task_config.ipynb)
1. [Task dependencies](Tutorials/3-Task-Dependencies/example.py)
1. [Flow execution](Tutorials/4-Flow-Execution/)
   1. [Task runners and Parallel execution](Tutorials/4-Flow-Execution/example.py)
   1. [Asynchronous execution](Tutorials/4-Flow-Execution/asyncio_execution.py)
1. [Dask and Ray task runners](Tutorials/5-Dask-Ray-Task-Runners/)
   1. [Sequential task runner](Tutorials/5-Dask-Ray-Task-Runners/sequential_flow.py)
   1. [Dask task runner](Tutorials/5-Dask-Ray-Task-Runners/dask_flow.py)
   1. [Ray task runner](Tutorials/5-Dask-Ray-Task-Runners/ray_flow.py)
   1. [Ray subflow task runner](Tutorials/5-Dask-Ray-Task-Runners/ray_subflow.py)
