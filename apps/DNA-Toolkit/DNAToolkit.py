# DNA Toolkit file

nucleotides = ["A", "C", "G", "T"]

# check a valid DNA string
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper() # uppercase version
    for nuc in nucleotides:
        if nuc not in tmpseq:
            return False
        return tmpseq

# count nucleotides frequency
def countNucFreq(dna_seq):
    temDictseq = {"A":0, "C":0, "G":0, "T":0}
    for nuc in dna_seq:
        temDictseq[nuc] += 1
    return temDictseq
        