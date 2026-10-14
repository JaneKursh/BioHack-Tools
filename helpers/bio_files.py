def extract_descripton(line: str) -> str:
    """
    Extracts a protein description from a BLAST line.
    Arguments:
        line: a detected string containing a protein description and other BLAST columns.
    Returns:
        a str with the protein description ending with '...' or ']' from description column only.
    """
    clean_string = ""
    for symbol in line:   
        clean_string += symbol
        if clean_string.endswith('...') or clean_string.endswith(']'):
            break
    return clean_string