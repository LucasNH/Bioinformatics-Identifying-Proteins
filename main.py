# This program was authored by Lucas Noritomi-Hartwig, November 2, 2022,
# to be used as a helpful tool for those studying bioinformatics, or for
# those who are interested in the field.

# Instructions are posted in the README.md file.

import os

START_CODON = "TAC"
STOP_CODONS = ["ATC", "ATT", "ACT"]

dir = "sequences"

def main():
    """
    Iterate through each sequence file in directory <dir>, and identify
    each possible protein in the sequence file.
    """
    print("\nIdentifying proteins...")

    for file in os.listdir(dir):
        # Filter for sequence files.
        if (file[:9] == "sequence_") and file.endswith(".txt"):
            id_proteins(file)
    
    print("\nProteins identified\n")


def id_proteins(file):
    """
    Read the sequnce in <file> and identify proteins by flagging start
    and stop codons.
    """

    # Open file in directory <dir>.
    relative_file = os.path.join(dir, file)
    f = open(relative_file, "r")
    sequence = f.read()
    f.close()

    # Parse the sequence into codons (three consecutive nitrogenous bases).
    n = len(sequence)
    parsed_seq = [sequence[i - 3:i] for i in range(3, n + 3, 3)]

    # Flag start and stop codons in parsed sequence.
    sequence_flagged = flag_codons(parsed_seq, len(parsed_seq))

    # Output flagged sequence to file.
    out_file = "identified_" + file
    relative_out_file = os.path.join(dir, out_file) 
    f_out = open(relative_out_file, "w")
    f_out.write(sequence_flagged)
    f_out.close()


def flag_codons(p_seq, n):
    """
    Flag start and stop codons with '*' and '**', respectively.
    """

    # Split the seqeunce into a list and initialize the flagged sequence.
    seq_flagged = ""

    # Identify all start and stop codons and flag accordingly.
    for i in range(n):
        codon = p_seq[i]

        # Append codon and appropriate flag to flagged sequence
        seq_flagged += codon + ("*" * (codon == START_CODON)) + \
            ("**" * (codon in STOP_CODONS)) + "/"
    
    return seq_flagged[:-1]


if __name__ == "__main__":
    main()
