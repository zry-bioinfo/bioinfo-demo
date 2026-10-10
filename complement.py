def complement(sequence):
    # This function takes a DNA sequence as input and returns its complementary sequence.
    sequence = sequence.upper()  # Convert the sequence 
    complement_dict={'A':'T','T':'A','C':'G','G':'C','N':'N'}
    complement_sequence = ""
    for base in sequence:
        complement_sequence += complement_dict[base]
    return complement_sequence
#测试
if __name__ == "__main__":
    test_sequence = "ATCG"
    print(f"Original sequence: {test_sequence}")
    print(f"Complementary sequence: {complement(test_sequence)}")
def reverse_complement(sequence):
    # This function takes a DNA sequence as input and returns its reverse complementary sequence.
    complement_sequence = complement(sequence)  # Get the complementary sequence
    reverse_complement_sequence = complement_sequence[::-1]  # Reverse the complementary sequence
    return reverse_complement_sequence
#测试
if __name__ == "__main__":
    test_sequence = "ATCG"
    print(f"Original sequence: {test_sequence}")
    print(f"Reverse complementary sequence: {reverse_complement(test_sequence)}")