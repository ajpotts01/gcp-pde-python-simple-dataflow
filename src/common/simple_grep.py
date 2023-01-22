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
