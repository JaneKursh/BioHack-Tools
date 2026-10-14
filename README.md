## **🧪 BioHack Tools**

Useful scripts, less manual work 👌

BioHack Tools is a lightweight Python utility for working with biological sequence data. The project combines simple tools for reading, filtering and transforming common bioinformatics file formats like FASQ, FASTA and BLAST.

Built with Python and educational passion 💓.

### 🧩 **Project structure**

```text
BioHack Tools/
├── README.md
├── main.py    # Utilities, imports, filter_fastq and Part B functions
└── helpers/
    ├── fastq.py        # Helper🔸 functions for filter_fastq()
    └── bio_files.py    # Helper🔹 function for parse_blast_output()
```

### 🧩 **Toolkit**

**Functions** used in this program:



   | Function                                          | Superpower  | 
   | -------------                                     |:-------------:|
   | `🔶filter_fastq()`   |  Filters reads by length, GC percentage and average quality |  
   | `🔸fastq_reader()`    | Reads one record from a FASTQ file  |
   | `🔸length_check()`       | Checks whether a sequence length meets specified limits |
   | `🔸gc_check()`         |Checks whether the GC percentage complies with the specified bounds |
   | `🔸quality_check` | Checks whether the average quality score complies with the specified threshold |
   | `🔷convert_multiline_fasta_to_oneline()` | Converts multiline FASTA sequences into single-line sequences |
   | `🔷parse_blast_output()`   |  Extracts the first protein description from each BLAST result section and sorts the descriptions alphabetically|
   |`🔹extract_descripton()`      | Extracts a protein description from a BLAST result line  |


### 🧩 **Getting started**


Clone the repository to your local machine:

`git clone https://github.com/JaneKursh/BioHack-Tools.git`

`cd BioHack-Tools`

Create a Python script in the project root, then you can import functions from main.py like this:

```text
from main import parse_blast_output

parse_blast_output(
    input_file="example_blast_results.txt",
    output_file="protein_descriptions.txt"
)
```

Make sure that **Python 3.10** or newer is installed!