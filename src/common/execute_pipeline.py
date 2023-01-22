from common.simple_grep import simple_grep

import apache_beam as beam


def execute_pipeline(arguments: list[str], input_path: str, output_path: str):
    """
    Main pipeline. Uses a beam.FlatMap call + a simple grep generator method to demonstrate pulling search terms out of lines of text.

    :param list[str] arguments: Pipeline arguments per the Apache Beam/GCP Dataflow standard.
    """
    print("Started pipeline")
    print(arguments)
    pipeline = beam.Pipeline(argv=arguments)
    search_term = "Integer"

    (
        pipeline
        | "ReadWords" >> beam.io.ReadFromText(file_pattern=input_path)
        | "SimpleGrep"
        >> beam.FlatMap(
            lambda next_line: simple_grep(text_line=next_line, search_term=search_term)
        )
        | "WriteToFile" >> beam.io.WriteToText(file_path_prefix=output_path)
    )

    pipeline.run().wait_until_finish()
