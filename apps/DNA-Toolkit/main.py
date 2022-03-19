# code testing
from DNAToolkit import *
import random

#rndDNAstr = "ATTTCcgtT"

# generate random string
rndDNAstr = ''.join([random.choice(nucleotides) for nuc in range(50)])

# validate DNA sequence
#print(validateSeq(rndDNAstr))
DNAstr = validateSeq(rndDNAstr) # make sure working with a validated string

# count nucleotides frequency
print(countNucFreq(DNAstr))