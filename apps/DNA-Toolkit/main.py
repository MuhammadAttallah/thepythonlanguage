# code testing
from DNAToolkit import *
import random

#rndDNAstr = "ATTTCcgtT"
rndDNAstr = ''.join([random.choice(nucleotides) for nuc in range(20)])

# generate random string
print(validateSeq(rndDNAstr))