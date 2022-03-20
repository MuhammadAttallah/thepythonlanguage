# code testing
from DNAToolkit import *
from utilities import colored
import random

#rndDNAstr = "ATTTCcgtT"

# generate random string for testing
rndDNAstr = ''.join([random.choice(nucleotides) for nuc in range(50)])

DNAstr = validateSeq(rndDNAstr) # make sure working with a validated string

print(f"\nSequence: {colored(DNAstr)}\n")
print(f"[1] + Sequence Length: {len(DNAstr)}\n")
print(colored(f"[2] + Nucleotide Frequency: {countNucFreq(DNAstr)}\n"))
print(f"[3] + DNA/RNA Transcription: {colored(transcription(DNAstr))}\n")
print(f"[4] + DNA String + Reverse Complement:\n5' {colored(DNAstr)} 3'")
print(f"   {''.join(['|' for c in range (len(DNAstr))])}")
print(f"3' {colored(reverse_complement(DNAstr))} 5'\n")