# Standard lib imports
import os
import sys

# Third-party lib imports
import apache_beam as beam

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


def simple_grep(text_line: str, search_term: str):
    """
    Loosely searches a line of text for a specified search term.

    This is based on Google's Apache Beam example which only checks for the term at start of a line.

    :param str text_line: Line of text to search
    :param str search_term: Term to find in the text
    :return str text_line: Lines of text starting with the search term
    """

    # Using a generator
    # https://beam.apache.org/documentation/transforms/python/elementwise/flatmap/#example-4-flatmap-with-a-generator
    if text_line.startswith(search_term):
        yield text_line


def execute_pipeline(arguments: list[str]):
    """
    Main pipeline. Uses a beam.FlatMap call + a simple grep generator method to demonstrate pulling search terms out of lines of text.

    :param list[str] arguments: Pipeline arguments per the Apache Beam/GCP Dataflow standard.
    """
    print("Started pipeline")
    pipeline = beam.Pipeline(argv=arguments)
    input = "../search_files/words.txt"
    path = f"{OUTPUT_PATH}/{OUTPUT_PREFIX}"
    search_term = "Integer"

    (
        pipeline
        | "ReadWords" >> beam.io.ReadFromText(file_pattern=input)
        | "SimpleGrep"
        >> beam.FlatMap(
            lambda next_line: simple_grep(text_line=next_line, search_term=search_term)
        )
        | "WriteToFile" >> beam.io.WriteToText(file_path_prefix=path)
    )

    pipeline.run().wait_until_finish()


if __name__ == "__main__":
    clear_folder(OUTPUT_PATH)
    execute_pipeline(arguments=sys.argv)
