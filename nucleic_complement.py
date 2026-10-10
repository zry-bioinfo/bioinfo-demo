#有DNA-->DNA(复制)，DNA-->RNA(转录）,RNA-->DNA(逆转录)，RNA-->RNA(复制)四种碱基互补配对方式。在这个程序中，我们将实现一个简单的碱基互补配对功能，用户可以输入一个DNA或RNA序列，程序将输出其互补序列。
pair_rules={
    "dna2dna": {"A": "T", "T": "A", "C": "G", "G": "C", "N": "N"},
    "dna2rna": {"A": "U", "T": "A", "C": "G", "G": "C",'N': "N"},
    "rna2dna": {"A": "T", "U": "A", "C": "G", "G": "C",'N': "N"},
    "rna2rna": {"A": "U", "U": "A", "C": "G", "G": "C",'N': "N"}
}#四种转换配对规则
def nucleic_complement(sequence, conversion_type):
    """
    根据指定的转换类型返回互补序列。
    
    参数:
    sequence (str): 输入的DNA或RNA序列。
    conversion_type (str): 转换类型，可以是 "dna2dna", "dna2rna", "rna2dna", "rna2rna"。
    
    返回:
    str: 互补序列。
    """
    if conversion_type not in pair_rules:
        raise ValueError("无效的转换类型。请选择 'dna2dna', 'dna2rna', 'rna2dna', 或 'rna2rna'。")
    
    complement_sequence = ""
    for base in sequence.upper():
        if base in pair_rules[conversion_type]:
            complement_sequence += pair_rules[conversion_type][base]
        else:
            raise ValueError(f"无效的碱基: {base}")
    
    return complement_sequence
# 示例用法
if __name__ == "__main__":
    # 测试 DNA 到 DNA 的转换
    dna_sequence = "ATCGN"
    complement_dna = nucleic_complement(dna_sequence, "dna2dna")
    print(f"原始序列: {dna_sequence}")
    print(f"互补序列: {complement_dna}")
    # 测试 DNA 到 RNA 的转换
    complement_rna = nucleic_complement(dna_sequence, "dna2rna")
    print(f"原始序列: {dna_sequence}")
    print(f"互补序列: {complement_rna}")    
    # 测试 RNA 到 DNA 的转换
    rna_sequence = "AUCGN"  
    complement_dna_from_rna = nucleic_complement(rna_sequence, "rna2dna")
    print(f"原始序列: {rna_sequence}")
    print(f"互补序列: {complement_dna_from_rna}")       
    # 测试 RNA 到 RNA 的转换
    complement_rna_from_rna = nucleic_complement(rna_sequence, "rna2rna")
    print(f"原始序列: {rna_sequence}")  
    print(f"互补序列: {complement_rna_from_rna}")
    #预期结果：
    # 原始序列: ATCGN
    # 互补序列: TAGCN
    # 原始序列: ATCGN
    # 互补序列: UAGCN
    # 原始序列: AUCGN
    # 互补序列: TAGCN
    # 原始序列: AUCGN
    # 互补序列: UAGCN