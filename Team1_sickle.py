import sys
import doctest
from better_sickle_kerensa import fastq_read
# need to import our function and class definition files?

'''Usage is 
$python Team1_sickle.py <FASTQ filename>
'''

def get1block(file):
    line1 = file.readline().rstrip()
    line2 = file.readline().rstrip()
    line3 = file.readline().rstrip()
    line4 = file.readline().rstrip()
    fq_obj = fastq_read(line1, line2, line4)
    return fq_obj
    
try:
    file = open(sys.argv[1])
except:
    print'There was a problem opening the FASTQ file. Filename: '+ sys.argv[1]
print get1block(file).name
