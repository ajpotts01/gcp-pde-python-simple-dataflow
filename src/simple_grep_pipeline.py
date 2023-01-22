# Standard lib imports
import os
import sys

# Project lib imports
from common.execute_pipeline import execute_pipeline

OUTPUT_PATH = "../results"
OUTPUT_PREFIX = "results"


def clear_folder(path: str):
    """
    Deletes all files in the selected path.

    :param str target: path to clear out.
    """
    for next_file in os.listdir(path):
        # Just supplying the filename to the os methods is not sufficient
        full_path: str = f"{path}/{next_file}"
        print(f"Deleting {next_file}")
        if os.path.isfile(full_path):
            os.unlink(full_path)


def run():
    input_path = "../search_files/words.txt"
    output_path = f"{OUTPUT_PATH}/{OUTPUT_PREFIX}"
    execute_pipeline(arguments=sys.argv, input_path=input_path, output_path=output_path)


if __name__ == "__main__":
    clear_folder(OUTPUT_PATH)
    run()
