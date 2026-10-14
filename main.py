import os

from helpers.fastq import (fastq_reader, length_check, gc_check, quality_check)
from helpers.bio_files import (extract_descripton)

def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds: int | float | tuple = (0, 100),
    length_bounds: int | tuple = (0, 2**32),
    quality_threshold: int = 0):
    
    """
    Filters FASTQ reads according to GC percentage, length and average quality score.
    Arguments:
        input_fastq: the name or path of the input FASTQ file
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

def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str = None) -> None:
    """
    Converts a multiline FASTA file into file with oneline sequences.
    Arguments:
        input_fasta: the name or path of the input FASTA file
        output_fasta: the name or path of the output FASTA file. 
                      If name has not been given, the output file is named 'output_fasta.fasta'
    Returns:
        None. Writes converted sequences to a named output file.
    """
    if output_fasta is None:
        output_fasta = 'output_fasta.fasta'
    
    with open(input_fasta) as fasta_in, open(output_fasta, mode = 'w') as fasta_out:
        count = 0
        for line in fasta_in:
            if line.startswith('>') and count == 0:
                fasta_out.write(line)
                count += 1
            elif line.startswith('>') and count > 0:
                fasta_out.write('\n' + line)
            else:
                fasta_out.write(line.rstrip('\n'))

                

def parse_blast_output(input_file: str, output_file: str = None) -> None:
    """
    Extracts the first protein description for each BLAST query and writes them alphabetically sorted to a file.
    Arguments:
        input_file: the name or path of the input BLAST file
        output_file: the name or path of the output file. 
                    If name has not been given, the output file is named 'output_fasta.fasta'.
    Returns:
        None. Writes extracted and sorted descriptions to a named output file.   
    """
    if output_file is None:
        output_file = 'output_file.txt'
    
    with open(input_file) as blast_in, open(output_file, mode = 'w') as blast_out:
        proteins = []
        for line in blast_in:
            
             if "Sequences producing significant alignments:" in line:
                for i in range(3):
                    line = next(blast_in)
                protein = extract_descripton(line)
                proteins.append(protein)
                 
        proteins.sort()
        for protein in proteins:
            blast_out.write(protein + '\n')
                    
            
        
    
    