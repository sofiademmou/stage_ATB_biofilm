import re, sys
from Bio import SeqIO
import csv
import pandas as pd

dico_S80I={}
dico_E84V={}
#dic_aa_posi={"Decalage" : 0, "D82" : dico_D82, "S83" : dico_S83,"D87" : dico_D87}

def mutations_gyrA(ref,ech,ech_out_1,ech_out_2):
    seq=SeqIO.read(ref, 'fasta')
    seq_ref=seq.seq
    print(seq_ref)

    muta=0
    reads=0
    decalage=0

    for seqRecord in SeqIO.parse(ech, 'fasta'):
        reads+=1
        seq_ech=seqRecord.seq
        name=seqRecord.description
        #print(seq_ech)
        for i in range(len(seq_ref)):
            if i==72:
                aa=seq_ech[i]
                print(aa)
                #if aa!="-":
                if aa!="-" and aa!="S":
                    S80="ok"
                    muta+=1
                    if aa in dico_S80I:
                        dico_S80I[aa]+=1
                    else:
                        dico_S80I[aa]=1
                else:
                    #print("Décalage")
                    decalage+=1

            elif i==76:
                aa=seq_ech[i]
                #if aa!="-":
                if aa!="-" and aa!="E":
                    if S80!="ok":
                        muta+=1
                    if aa in dico_E84V:
                        dico_E84V[aa]+=1
                    else:
                        dico_E84V[aa]=1
                else:
                    #print("Décalage")
                    decalage+=1
    dic_aa_posi={"Decalage" : decalage, "S80I" : dico_S80I,"E84V" : dico_E84V}
    print(dic_aa_posi)
    muta_S80I={}
    muta_E84V={}
    """
    for i in dico_S80I:
        muta_S80I[i] = round(float(dico_S80I[i]/reads)*100,2)
    for i in dico_E84V:
        muta_E84V[i] = round(float(dico_E84V[i]/reads)*100,2)
    dic_muta_aa_posi={"Decalage" : round(float(decalage/reads)*100,2), "S80I" : muta_S80I,"E84V" : muta_E84V}
    """
    
    for i in dico_S80I:
        muta_S80I[i] = round(float(dico_S80I[i]/muta)*100,2)
    for i in dico_E84V:
        muta_E84V[i] = round(float(dico_E84V[i]/muta)*100,2)
    dic_muta_aa_posi={"Decalage" : round(float(decalage/muta)*100,2), "S80I" : muta_S80I,"E84V" : muta_E84V}
    
    print(dic_muta_aa_posi)
    #print(reads)
    df2 = pd.DataFrame(data=muta_S80I, index=[0])
    df2 = (df2.T)
    df2.to_excel(ech_out_1)
    df3 = pd.DataFrame(data=muta_E84V, index=[0])
    df3 = (df3.T)
    df3.to_excel(ech_out_2)




##Test
ref=sys.argv[1]

ech=sys.argv[2]

ech_out_1=sys.argv[3]

ech_out_2=sys.argv[4]

mutations_gyrA(ref,ech,ech_out_1,ech_out_2)







