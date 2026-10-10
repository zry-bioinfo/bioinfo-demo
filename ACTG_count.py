def ACTG_count(seq):
    """Counts the number of occurrences of each nucleotide in a DNA sequence."""
    # Initialize a dictionary to hold the counts
    seq=seq.upper()  # Convert the sequence to uppercase to handle lowercase input
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    # Iterate through each nucleotide in the sequence
    for nucleotide in seq:
        if nucleotide in counts:
            counts[nucleotide] += 1

    return counts
#测试
if __name__ == "__main__":
    # Example usage
    dna_sequence = "ACGTACGTAGCTAGCTAGCTAGCTAGCTAGC"
    result = ACTG_count(dna_sequence)
    print(result)  # Output: {'A': 8, 'C': 8, 'G': 8, 'T': 7}