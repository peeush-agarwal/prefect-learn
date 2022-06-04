from prefect.deployments import DeploymentSpec
from prefect.flow_runners import SubprocessFlowRunner

DeploymentSpec(
    name="leonardo-deployment",
    flow_location="./leo_flow.py",
    tags=["tutorial", "test"],
    parameters={'name':'Leo'}
)

DeploymentSpec(
    name="marvin-deployment",
    flow_location="./leo_flow.py",
    tags=["tutorial", "dev"],
    flow_runner=SubprocessFlowRunner(),
    parameters={'name':'Marvin'}
)