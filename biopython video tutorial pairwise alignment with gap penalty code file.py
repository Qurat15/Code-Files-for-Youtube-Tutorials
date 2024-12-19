#!/usr/bin/env python
# coding: utf-8

# In[10]:


from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Function for pairwise alignment with gap penalties
def pairwise_alignment(seq1, seq2, alignment_type="global", gap_open=-2, gap_extend=-1, match=1, mismatch=-1):
    
    if alignment_type == "global":
        alignments = pairwise2.align.globalms(seq1, seq2, match, mismatch, gap_open, gap_extend)
    elif alignment_type == "local":
        alignments = pairwise2.align.localms(seq1, seq2, match, mismatch, gap_open, gap_extend)
    else:
        raise ValueError("Invalid alignment type. Choose 'global' or 'local'.")

    # Print and return alignments
    print("\nPairwise Alignments with Gap Penalties:")
    for alignment in alignments:
        print(format_alignment(*alignment))

# Example DNA sequences
dna_seq1 = "ACGTGTC"
dna_seq2 = "ACGTTGC"

# Perform pairwise alignment with gap penalties
pairwise_alignment(dna_seq1, dna_seq2, alignment_type="global", gap_open=-2, gap_extend=-1)


# In[ ]:


# diff bw gap open and gap extend

