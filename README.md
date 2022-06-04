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
1. Create a work queue: `prefect work-queue create --tag tutorial tutorial_queue`
   1. Note that this command specifically creates a "tutorial" tag on the work queue, meaning the tutorial_queue work queue will only serve deployments that include a "tutorial" tag. This is a good practice to make sure flow runs for a given deployment run only in the correct environments, based on the tags you apply.
   1. The Prefect API creates the work queue and returns the ID of the queue. Note this ID, you'll use it in a moment to create an agent that polls for work from this queue.
1. List of available work queues: `prefect work-queue ls`
1. Run agent: `prefect agent start 'c86c2f96-f366-498c-acee-d9c8e310ec52'`

Remember that:
1. The deployment specification included a "tutorial" tag.
1. The `tutorial_queue` work queue is defined to serve deployments with a "tutorial" tag.
1. The agent is configured to pick up work from `tutorial_queue`, so it will only execute flow runs for deployments with a "tutorial" tag.

### Run an orchestrated deployment

With a work flow and agent in place, you can create a flow run for `leonardo_dicaprio_flow` directly from the UI. Go back to the Prefect UI in your browser and click the __Quick Run__ button next the deployment.

### Add another deployment

1. Update [leo_deployment.py](Tutorials/6-Deployments/leo_deployment.py) with another DeploymentSpec
1. Create the deployment: `prefect deployment create leo_deployment.py`
   1. It won't change leonardo_deployment, but it will create a new marvin-deployment.
      1. Running `leonardo_deployment` logs the message "Hello Leo!".
      1. Running `marvin-deployment` logs the message "Hello Marvin!".
      1. `marvin-deployment` uses the `SubprocessFlowRunner`.
1. Both deployments can use the `tutorial_queue` work queue because they have "tutorial" tags. But if you created a new work queue that served deployments with, say, a "dev" tag, only `marvin-deployment` would be served by that queue and its agents.

### Cleaning up

1. To terminate the agent, simply go to the terminal session where it's running and end the process with either `Ctrl+C` or by terminating the terminal session.
1. To pause a work queue, run the Prefect CLI command `prefect work-queue pause`, passing the work queue ID.
1. To delete a work queue, run the command `prefect work-queue delete`, passing the work queue ID.
1. To terminate the Prefect API server, go to the terminal session where it's running and end the process with either `Ctrl+C` or by terminating the terminal session.