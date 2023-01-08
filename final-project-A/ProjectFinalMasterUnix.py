#!/usr/bin/env python
# coding: utf-8

# In[ ]:


stop_codons = ["TAG", "TAA", "TGA", "tag", "taa", "tga"]


# In[ ]:


start_codon = ["ATG", "atg"]


# In[ ]:


seq = input("Provide DNA sequence: ")


# In[ ]:


i=0
j=0


# In[ ]:


orf_seq = ''


# In[ ]:


while (i < len(seq)-2):
    
    if (seq[i:i+3] not in start_codon):
        
        i+=1
        
        j=1
    
    elif (seq[i:i+3] in start_codon):
        
        orf_seq=''
        
        while seq[i:i+3] not in stop_codons and i<len(seq)-2:
            
            codon = seq[i:i+3]
            
            orf_seq = orf_seq + codon
            
            i+=3 
        
        if seq[i:i+3] in stop_codons:
            
            codon = seq[i:i+3]
            
            orf_seq = orf_seq + codon 
            
            print("The following open reading frame has been found in the sequence\n", orf_seq)
        
        else:
            
            i=j
            
            i+=1
            
            orf_seq=''

if not orf_seq:
    
    print("There is no open reading frame in the DNA sequence")

