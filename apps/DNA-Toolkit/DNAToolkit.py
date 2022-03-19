# DNA Toolkit file

nucleotides = ["A", "C", "G", "T"]
DNA_ReverseComplement = {"A":"T", "T":"A", "G":"C", "C":"G"}

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

# DNA to RNA transcription
def transcription(dna_seq):
    return dna_seq.replace("T", "U")
        
# reverse complement for replication
def reverse_complement(dna_seq):
    # swap then reverse
    return ''.join([DNA_ReverseComplement[nuc] for nuc in dna_seq])[::-1]