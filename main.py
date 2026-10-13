import os

from helpers.fastq import (fastq_reader, length_check, gc_check, quality_check)

def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds: int | float | tuple = (0, 100),
    length_bounds: int | tuple = (0, 2**32),
    quality_threshold: int = 0):
    
    """
    Filters FASTQ reads according to GC percentage, length and average quality score.

    Arguments:
        input_fastq: the path to the input FASTQ file
        output_fastq: the name of the output file.
        gc_bounds: the maximum GC percentage or a tuple containing the minimum and maximum GC percentages.
        length_bounds: the maximum sequence length or a tuple containing the minimum and maximum lengths.
        quality_threshold: the minimum allowed average quality score.
    Returns:
        None. Writes the filtered reads to a named output file.
    """
    
    if not os.path.exists("filtered"):
        os.mkdir("filtered")
    output_path = os.path.join("filtered", output_fastq)

    with open(input_fastq) as fin, open(output_path, mode='w') as fout:
        while True:
            read = fastq_reader(fin)

            if read is None:
                break

            read_id, sequence, separator, quality = read

            gc_is_valid = gc_check(sequence, gc_bounds)
            length_is_valid = length_check(sequence, length_bounds)
            quality_is_valid = quality_check(quality, quality_threshold)

            if gc_is_valid and length_is_valid and quality_is_valid:
                fout.write(read_id + '\n')
                fout.write(sequence + '\n')
                fout.write(separator + '\n')
                fout.write(quality + '\n')
                