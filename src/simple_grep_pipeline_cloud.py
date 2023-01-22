# Standard lib imports
import os

# Project lib imports
from common.execute_pipeline import execute_pipeline

# Third-party lib imports
from dotenv import load_dotenv

ENV_PATH = "pipeline.env"
ENV_KEY_PROJECT = "GCP_PROJECT"
ENV_GCS_BUCKET = "GCS_BUCKET"


def clear_folder(path: str):
    pass


def get_cloud_config() -> list[str]:
    project: str = os.getenv(ENV_KEY_PROJECT)
    bucket: str = os.getenv(ENV_GCS_BUCKET)

    staging_path = f"gs://{bucket}/staging"

    cloud_config = [
        f"--project={project}",
        f"--job_name=gcp-pde-python-simple-dataflow",
        "--save_main_session",
        f"--staging_location={staging_path}",
        f"--temp_location={staging_path}",
        "--region=australia-southeast1",
        "--runner=DataFlowRunner",
        "--setup_file=./setup.py"
    ]

    return cloud_config

def run():
    load_dotenv('pipeline.env')
    arguments: list[str] = get_cloud_config()
    bucket: str = os.getenv(ENV_GCS_BUCKET)
    input_path = f"gs://{bucket}/search_files/words.txt"
    output_path = f"gs://{bucket}/results/results"

    execute_pipeline(arguments=arguments, input_path=input_path, output_path=output_path)


if __name__ == "__main__":
    clear_folder("")
    run()
