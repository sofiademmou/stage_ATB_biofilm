import re,sys
from Bio import SeqIO
import csv
import pandas as pd

dico_co_occ={"S80I" : 0, "E84V" : 0, "co_occurence" : 0}


def mutations_gyrA(ref,ech,ech_out):
    seq=SeqIO.read(ref, 'fasta')
    seq_ref=seq.seq

    muta=0
    reads=0


    for seqRecord in SeqIO.parse(ech, 'fasta'):
        i=0
        S80I=""
        E84V=""
        reads+=1
        seq_ech=seqRecord.seq
        name=seqRecord.description
        while i <len(seq_ref):
            if i==72:
                #on met en key la position pour les mutations à cette position
                aa=seq_ech[i]
                if aa=="I":
                    S80I="OK"
                    dico_co_occ["S80I"]+=1
                i+=1
            elif i==76:
                #on met en key la position pour les mutations à cette position
                aa=seq_ech[i]
                if aa=="V":
                    E84V="OK"
                    dico_co_occ["E84V"]+=1
                i+=1
            elif i==88:
                if S80I=="OK" and E84V=="OK":
                    dico_co_occ["co_occurence"]+=1
                i+=1
            else:
                i+=1

        print(dico_co_occ)

    my_dict={}
    for i in dico_co_occ:
            my_dict[i] = round(float(dico_co_occ[i]/reads)*100,2)
    #my_dict["S80I seul"]=my_dict["S80I"]-my_dict["co_occurence"]
    my_dict["S80I + E84V"]=my_dict["co_occurence"]/my_dict["S80I"]*100
    my_dict["E84V + S80I"]=my_dict["co_occurence"]/my_dict["E84V"]*100
    print(my_dict)
    print(reads)

    df = pd.DataFrame(data=my_dict, index=[0])
    df = (df.T)
    df.to_excel(ech_out)




##Execution
ref=sys.argv[1]

ech=sys.argv[2]

ech_out=sys.argv[3]

mutations_gyrA(ref,ech,ech_out)







