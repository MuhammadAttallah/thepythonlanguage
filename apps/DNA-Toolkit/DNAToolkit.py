# DNA Toolkit file

nucleotides = ["A", "C", "G", "T"]

# check a valid DNA string
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper() # uppercase version
    for nuc in nucleotides:
        if nuc not in tmpseq:
            return False
        return tmpseq


        