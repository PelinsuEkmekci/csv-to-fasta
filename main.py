import pandas as pd
import os

PIPENN_FILE = "/Users/pelinsuekmekci/PycharmProjects/csv2fasta/"


def nsp():

    for file in os.listdir("/Users/pelinsuekmekci/PycharmProjects/csv2fasta/"):
        if file.endswith(".csv"):
            name = file.split('.')[0] + '' + '.fasta'
            f = open(name, 'w')       # create new file for fasta format
            pelin = PIPENN_FILE + file
            df = pd.read_csv(pelin)
            print(df.count())

            seq_col = df['sequence']
            uniprot_col = df['uniprot_id']
            pipenn_tuples = list(zip(range(len(seq_col)), seq_col, uniprot_col))
            for i, prot_seq, prot_id in pipenn_tuples:
                prot_seq = prot_seq.replace(',', '')
                f.write(">" + prot_id + ' id-' + str(i+1) + "\n")
                f.write(prot_seq + '\n')
            f.close()
if __name__ == "__main__":
    nsp()


