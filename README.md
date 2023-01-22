# Simple GCP Dataflow Pipeline using Python
Simple GCP Dataflow pipeline in Python from the official Google Professional Data Engineer certification material.

These are actually possible to do directly through Qwiklabs/Cloud Skills Boost, but the labs boil down to getting you to just run mostly pre-written code. I'm taking a different approach in reading the lab material, and writing it myself. Maybe adding CI/CD bells and whistles.

Original lab is [here on Cloud Skills Boost](https://www.cloudskillsboost.google/course_sessions/2329626/labs/358109). The pipeline uses Apache Beam 2.44.0, despite the lab being written for 2.5.0 (which is deprecrated).

There are two files that can be run independently to execute Apache Beam pipelines:
- `src\simple_grep_pipeline.py`, for local running
- `src\simple_grep_pipeline_cloud.py`, for running on Google Cloud Dataflow

Steps before running either pipeline:
1. Clone the repo
2. Create and activate a Python virtual environment
3. Run `pip install -r requirements.txt` from the root directory
4. Set your `PYTHONPATH` to the `src` folder
    - Change directory to the `src` folder
    - On bash, `export PYTHONPATH=$(cwd)`
    - On Powershell, `$env:PYTHONPATH = Get-Location`

If running locally:
1. Run `python simple_grep_pipeline.py`
2. Check the `results` folder

If running on Google Cloud Dataflow:
1. Set up a Google Cloud Platform account
2. Create a Google Cloud Storage bucket for this project
3. Install the Google Cloud SDK
4. Set your application default credentials by running `gcloud auth application-default login`
5. Create a `pipeline.env` file in `src`, with the following keys:
    - `GCP_PROJECT`: Your GCP project ID from step 1
    - `GCS_BUCKET`: Your GCS bucket from step 2
6. Run `python simple_grep_pipeline_cloud.py`
7. Check the `results` folder in your GCS bucket.