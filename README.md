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

## Deployment tutorial

1. Create a script with the flow. [leo.py](Tutorials/6-Deployments/leo_flow.py)
1. Create a deployment specification for this flow. [leo_deployment.py](Tutorials/6-Deployments/leo_deployment.py)
1. Set the Prefect API server URL: `prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api`
1. Configure storage: `prefect storage create`
   1. Make sure the bucket already exists in S3 buckets.
1. Create the deployment: `prefect deployment create leo_deployment.py`
1. List all of the current deployments: `prefect deployment ls`
1. Display details of the specific deployment: `prefect deployment inspect 'leonardo_dicaprio_flow/leonardo-deployment'`
1. Run the deployment locally: `prefect deployment execute leonardo_dicaprio_flow/leonardo-deployment`
   1. Format of the name: flow_name/deployment_name
   1. Flow may be referenced by multiple deployments, each deployment must have a unique name.
1. View the deployment in Prefect UI: [Deployments](http://127.0.0.1:4200/#deployments)

