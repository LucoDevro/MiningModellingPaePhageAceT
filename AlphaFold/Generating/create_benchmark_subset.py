from Bio import SeqIO
import random

with open("all.fasta", "r") as fasta_handle:
    prots = list(SeqIO.parse(fasta_handle, "fasta"))

random.seed(127)
sel = random.sample(range(len(prots)), 20)
for i in sel:
    name = prots[i].id
    with open('.'.join([name, "fasta"]), "w") as handle:
        SeqIO.write(prots[i], handle, "fasta")