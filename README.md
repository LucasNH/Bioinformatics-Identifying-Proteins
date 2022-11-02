# Bioinformatics-Identifying-Proteins
This program was authored by Lucas Noritomi-Hartwig, November 2, 2022.

The program will identify possible proteins in DNA sequences by flagging start and stop codons with "*" and "**", respectively.

## Setup:
1) For each sequence, create a file named "sequence_X.txt" where X is the sequence number (have as many as you like).
2) In the created text file, paste the entire sequence (without codon separation, spaces, newlines, etc.) into the first line.
3) Store the text file in a directory named "sequences" which itself is to be stored in the same directory as main.py

## Running main.py
1) Open a terminal at the directory holding the main.py file and sequences directory, and run the following command:
```
python3 main.py
```
2) In the sequences directory, for each "sequences_X.txt" file will appear an "identified_sequence_X.txt" file with proper separation of codons, and appropriate flagging of start and stop codons.
