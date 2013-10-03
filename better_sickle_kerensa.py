class fastq_read:
    ''' Stores the name, nucleotide sequence, and encoded quality sequence for a fastq read'''
    
    def __init__(self,name,nuc_seq,qual_seq):
        self.nucleotides=nuc_seq
        self.qualities=qual_seq
        self.name=name
        
    
        
def decode_quality(char_str, offset):
    ''' Takes fastq quality string of characters from a fastq_read object, 
        and the relevent offset (i.e. 33 for Phred-33, 64 for Phred-64).
        Returns a list of integers representing 
        phred encoded quality scores (character's ascii value minus offset) '''
       
        phred=[]
        
        for c in char_str:
            phred.append(ord(c)-offset)
            
        return phred
        
              
