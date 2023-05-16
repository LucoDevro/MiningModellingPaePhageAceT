#!/usr/bin/env python3

import sys
from Bio import SeqIO
with open(sys.argv[1], "r") as handle:
    records = SeqIO.to_dict(SeqIO.parse(handle, "fasta"))

processed_records = dict(records)
for label,record in records.items():
    if "*" in record.seq:
        processed_records.pop(label)
        
with open("PaePhages_CDSs_filtered.fasta", "w") as new_handle:
    SeqIO.write(processed_records.values(), new_handle, "fasta")
