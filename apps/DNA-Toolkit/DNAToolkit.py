# DNA Toolkit file

from mimetypes import init
from structures import *

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
    """"
    DNA -> RNA Transcription. 
    Replacing "T" Thymine with "U" Uracil
    """
    return dna_seq.replace("T", "U")
        
# reverse complement for replication
def reverse_complement(dna_seq):
    """
    Swapping Adenine with Thymine and Guanine with Cytosine. 
    Reversing newly generated string.
    """
    # swap then reverse
    return ''.join([DNA_ReverseComplement[nuc] for nuc in dna_seq])[::-1]

    # Pythonic approach
    # mapping = str.maketrans("ATCG", "TAGC")
    # return dna_seq.translate(mapping)[::-1]

def gc_content(dna_seq):
    """GC content in a DNA/RNA sequence"""
    return (dna_seq.count("C") + dna_seq.count("G") / len(dna_seq) * 100)

def gc_content_subsec(dna_seq, k=20):
    """"
    GC Content in a DNA/RNA sub-sequence length k.
    k=20 by default.
    """
    res = []
    for i in range(0, len(dna_seq) - k + 1, k):
        subseq = dna_seq[i:i+k]
        res.append(gc_content(subseq))
    return res

def translate_seq(dna_seq, init_pos):
    """Translates a DNA sequence into an aminoacid sequence"""
    return [DNA_Codons[dna_seq[pos:pos + 3]] for pos in range(init_pos, len(dna_seq) - 2, 3)]