import doctest

class fastq_read:
    ''' Stores the name, nucleotide sequence, and encoded quality sequence for a fastq read'''

    def __init__(self,name,nuc_seq,qual_seq):
        legal=set('ATGCNatgcn')
        assert set(nuc_seq).issubset(legal)
        assert len(nuc_seq)==len(qual_seq)
        self.nucleotides=nuc_seq
        self.qualities=qual_seq
        self.name=name
        
    
        
def decode_quality(char_str, offset):
    ''' Takes fastq quality string of characters from a fastq_read object, 
        and the relevent offset, and returns a list of integers representing 
        phred encoded quality scores (character's ascii value minus offset) 
        
        Legal offset values are: 
            33 (Sanger and Illumina 1.8+)
            64 (Solexa, Illumina 1.3, Illumina 1.5)
        
        Example:
        
        phred('A') = ascii value of 'A' minus the offset
        phred('A') = 65 - 33 (using offset of 33, for Sanger and Illumina 1.8+)
        
        >>> decode_quality("!\\"#$%&'()*+,", 33)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        >>> decode_quality("III", 64)
        [9, 9, 9]
        >>> decode_quality("III", 33)
        [40, 40, 40]
        >>> decode_quality("@", 33)
        [31]
        '''
       
    phred=[]
    legal_offset=set([33,64])
    
    try:
        assert offset in legal_offset
    except:
        print "Offset must be an integer, either 33 or 64"
        return Exception
    for c in char_str:
        phred.append(ord(c)-offset)
       
    return phred
        

        
if __name__ == "__main__":
    doctest.testmod()
              
