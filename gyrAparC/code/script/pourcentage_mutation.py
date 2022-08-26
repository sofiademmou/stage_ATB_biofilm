import re, sys
from Bio import SeqIO
import csv
import pandas as pd

dic_muta={"Nombre de mutations" : 0, "Nombre total de reads" : 0, "Pourcentage de mutation" : 0}
dic_muta_posi={"Decalage" : 0}
dic_aa_posi={}



def mutations_totales(ref,ech,ech_out):
    seq=SeqIO.read(ref, 'fasta')
    seq_ref=seq.seq
    print(seq_ref)

    muta=0
    reads=0

    for seqRecord in SeqIO.parse(ech, 'fasta'):
        i=0
        reads+=1
        seq_ech=seqRecord.seq
        name=seqRecord.description
        print(seq_ech)
        while i < len(seq_ref):
            #on met en key la position pour les mutations à cette position
            if seq_ech[i]!="-":
                #dic_muta_tot["Nombre total de reads"]+=1
                if seq_ref[i]!=seq_ech[i]:
                    #print("different")
                    #dic_muta_posi[i]+=muta
                    if i in dic_muta_posi:
                        dic_muta_posi[i]+=1
                        #dic_aa_posi[i]+=1
                    else:
                        dic_muta_posi[i]=1
                        #dic_muta_posi[i]+=1
                """
                else:
                    print("same")
                """
                i+=1
            else:
                #print("Décalage")
                dic_muta_posi["Decalage"]+=1
                i+=1
        print(dic_muta_posi)
    #a = {k: v / total for total in (sum(dic_muta_posi.values()),) for k, v in dic_muta_posi.items()}
    my_dict={}
    for i in dic_muta_posi:
            my_dict[i] = round(float(dic_muta_posi[i]/reads)*100,2)
    print(my_dict)
    print(reads)
    
    df = pd.DataFrame(data=my_dict, index=[0])
    df = (df.T)
    df.to_excel(ech_out)





#def mutations_position(position):





##Test
ref=sys.argv[1]

ech=sys.argv[2]

ech_out=sys.argv[3]

mutations_totales(ref,ech,ech_out)







