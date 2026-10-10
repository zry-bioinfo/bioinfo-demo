def gc_content(seq):
    """计算给定DNA序列的GC含量百分比。
    seq: str, DNA序列,只包含ATGC字符
    返回: float, GC含量百分比
    """
    #全部转为大写，防止小写输入错误
    seq = seq.upper()
    g=seq.count("G")
    c=seq.count("C")
    total=len(seq)
    if total == 0:
        return 0.0
    gc_percent = (g + c) / total * 100
    return gc_percent
#测试
if __name__ == "__main__":
    test1="AGCTATAG"
    test2="CGCGCGCG"
    test3="ATATATAT"  
    print(f"GC content of {test1}: {gc_content(test1):.2f}%")
    print(f"GC content of {test2}: {gc_content(test2):.2f}%")
    print(f"GC content of {test3}: {gc_content(test3):.2f}%")