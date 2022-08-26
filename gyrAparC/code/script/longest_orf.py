import sys
from Bio import SeqIO
import re

file = open(sys.argv[2],'w')
current_cid=""
first = "TRUE"
for record in SeqIO.parse(open(sys.argv[1]),"fasta"):
    l=1
    cid = str(record.description).split('_')[0][0:]
    seq=record.seq
    if str(cid)!=str(current_cid):
        current_cid=cid
        current_length=len(seq)
        #print(cid)
        #print("change")
        if first=="FALSE":
            file.write(">" + max_cid + "\n")
            file.write(str(max_seq[0:59]) + "\n" + str(max_seq[60:]) + "\n")
            first = "TRUE"
    else:
        if len(seq)>current_length:
        #if len(seq)>100:
            current_length=len(seq)
            max_cid=record.description
            max_seq=seq
    first = "FALSE"
file.write(">" + max_cid + "\n")
file.write(str(max_seq[0:59]) + "\n" + str(max_seq[60:]) + "\n")
file.close()
