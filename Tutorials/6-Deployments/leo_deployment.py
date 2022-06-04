from prefect.deployments import DeploymentSpec

DeploymentSpec(
    name="leonardo-deployment",
    flow_location="./leo_flow.py",
    tags=["tutorial", "test"],
    parameters={'name':'Leo'}
)