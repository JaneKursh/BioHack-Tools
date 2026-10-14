def fastq_reader(fin: TextIO) -> tuple[str, str, str, str]:
    
    """
    Reads one record from a FASTQ file.
    Arguments:
        fin: an opened file object.
    Returns:
        a tuple containing 4 strings: read id, sequence, separator and quality,
        None if the end of the file has been reached.
    """
    
    read_id = fin.readline()

    if read_id == "":
        return None

    sequence = fin.readline()
    separator = fin.readline()
    quality = fin.readline()

    read_id = read_id.rstrip("\n")
    sequence = sequence.rstrip("\n")
    separator = separator.rstrip("\n")
    quality = quality.rstrip("\n")
    
    return read_id, sequence, separator, quality

def length_check(sequence: str, length_bounds: int | tuple) -> bool:

    """
    Checks whether the sequence length complies with the specified bounds.
    Arguments: 
        sequence: str (a nucleotide sequence).
        length_bounds: int representing the max value or tuple containing two int values representing the allowed bounds (min,max).
    Returns: 
        True if sequence lenght corresponds to the given bounds,
        False otherwise.
    """
    
    if isinstance(length_bounds, int):
        min_length = 0
        max_length = length_bounds
    else:
        min_length = length_bounds[0]
        max_length = length_bounds[1]
        
    return min_length <= len(sequence) <= max_length


def gc_check(sequence: str, gc_bounds: int | float | tuple) -> bool:

    """
    Checks whether the GC percentage complies with the specified bounds.
    Arguments: 
        sequence: str (a nucleotide sequence).
        gc_bounds: int(float) representing the max value or tuple containing two int values representing the allowed bounds (min,max).
    Returns: 
        True if GC percentage corresponds to the given bounds,
        False otherwise.
    """
    
    if isinstance(gc_bounds, int) or isinstance(gc_bounds, float):
        min_gc = 0
        max_gc = gc_bounds
    else:
        min_gc = gc_bounds[0]
        max_gc = gc_bounds[1]
        
    gc_amount = sequence.count('G') + sequence.count('C')
    gc_percent = (gc_amount / len(sequence)) * 100
   
    return min_gc <= gc_percent <= max_gc

def quality_check(quality: str, quality_threshold: int) -> bool:

    """
    Checks whether the average quality score complies with the specified threshold.
    Arguments:
        quality: A string containing Phred+33 quality characters.
        quality_threshold: The minimum allowed average quality score.
    Returns:
        True if the average quality score is greater than or equal to the given threshold,
        False otherwise.
    """
    
    qual_sum = 0
    for symbol in quality: 
        qual_sum += ord(symbol) - 33
    qual_ave = qual_sum / len(quality)
    
    return qual_ave >= quality_threshold