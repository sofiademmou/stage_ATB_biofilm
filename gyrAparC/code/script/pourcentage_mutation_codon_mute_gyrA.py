import re, sys
from Bio import SeqIO
import csv
import pandas as pd

dico_S83={}
dico_D87={}
#dic_aa_posi={"Decalage" : 0, "D82" : dico_D82, "S83" : dico_S83,"D87" : dico_D87}

def mutations_gyrA(ref,ech,ech_out_1,ech_out_2):
    seq=SeqIO.read(ref, 'fasta')
    seq_ref=seq.seq
    print(seq_ref)

    muta_S83=0
    muta_D87=0
    reads=0
    decalage=0
    


    for seqRecord in SeqIO.parse(ech, 'fasta'):
        S83=""
        reads+=1
        seq_ech=seqRecord.seq
        name=seqRecord.description
        #print(seq_ech)
        for i in range(len(seq_ref)):
            if i==32:
                aa=seq_ech[i]
                print(aa)
                #if aa!="-":
                if aa!="-" and aa!="S":
                    muta_S83+=1
                    if aa in dico_S83:
                        dico_S83[aa]+=1
                    else:
                        dico_S83[aa]=1
                else:
                    #print("Décalage")
                    decalage+=1

            elif i==36:
                aa=seq_ech[i]
                #if aa!="-":
                if aa!="-" and aa!="D":
                    muta_D87+=1
                    if aa in dico_D87:
                        dico_D87[aa]+=1
                    else:
                        dico_D87[aa]=1
                else:
                    #print("Décalage")
                    decalage+=1
    dic_aa_posi={"Decalage" : decalage, "S83" : dico_S83,"D87" : dico_D87}
    print(dic_aa_posi)
    muta_S83L={}
    muta_D87N={}
    """
    for i in dico_S83:
        muta_S83[i] = round(float(dico_S83[i]/reads)*100,2)
    for i in dico_D87:
        muta_D87[i] = round(float(dico_D87[i]/reads)*100,2)
    dic_muta_aa_posi={"Decalage" : round(float(decalage/reads)*100,2), "S83" : muta_S83,"D87" : muta_D87}
    """
    
    for i in dico_S83:
        muta_S83L[i] = round(float(dico_S83[i]/muta_S83)*100,2)
    for i in dico_D87:
        muta_D87N[i] = round(float(dico_D87[i]/muta_D87)*100,2)
    dic_muta_aa_posi={"S83" : muta_S83L,"D87" : muta_D87N}
    
    print(dic_muta_aa_posi)
    print(reads)
    df2 = pd.DataFrame(data=muta_S83L, index=[0])
    df2 = (df2.T)
    df2.to_excel(ech_out_1)
    df3 = pd.DataFrame(data=muta_D87N, index=[0])
    df3 = (df3.T)
    df3.to_excel(ech_out_2)




##Test
ref=sys.argv[1]

ech=sys.argv[2]

ech_out_1=sys.argv[3]

ech_out_2=sys.argv[4]

mutations_gyrA(ref,ech,ech_out_1,ech_out_2)







