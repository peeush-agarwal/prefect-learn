"""
Usage: python asyncio_execution.py
"""

import asyncio
from prefect import flow, task

@task
async def print_values(values):
    for value in values:
        await asyncio.sleep(1)
        print(value, end=" ")

@flow
async def async_flow():
    await print_values([1, 2]) # Runs immediately
    coros = [print_values("abcd"), print_values("6789")]

    # asynchronously gather the tasks
    await asyncio.gather(*coros)

if __name__ == "__main__":
    asyncio.run(async_flow())
