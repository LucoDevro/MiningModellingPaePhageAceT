**Contents:**
- Bash Jupyter notebook splitting the multi-entry GenBank file `AllGenBank.gb` into separate genome GenBank files and scraping some metadata from these (host, accessions, CDS tags) using shell script `Splitter&Scraper.sh` (`Metadata&Genomes.ipynb`)
- Bash Jupyter notebook running the nhmmer mining algorithm for all *Pseudomonas* phage genomes in `AllGenBank.gb` (`nhmmer.ipynb`)
- Bash Jupyter notebook running the phmmer mining algorithm for all *Pseudomonas* phage genomes CDSs in `PaePhages_CDSs.fasta` (`phmmer.ipynb`)
- Python script (`supfam_preprocessing.py`) preprocessing the CDS fasta file `PaePhages_CDSs.fasta` for running a SUPERFAMILY search against it using InterProScan in Bash Jupyter notebook `SUPERFAMILY.ipynb`
- Bash Jupyter notebook running the HHblits mining algorithm for all *Pseudomonas* phage genomes CDSs in `PaePhages_CDSs.fasta`(`HHblits.ipynb`)
- Python Jupyter notebook aggregating all mining hit sequences into one general fastas file and files per pipeline (`Sequence aggregation.ipynb`)
- Bash Jupyter notebook running the phmmer mining algorithm for all *Pseudomonas* phage genomes CDSs after proteins without typical acetyltransferase structural features have been filtered out (`phmmer_revisit.ipynb`)
- Python Jupyter notebooks visualising properties of the mining hits, before and after filtering out the false positive hits (`./Visualisation/Mining plotting.ipynb` & `./Visualisation/Mining plotting - TP.ipynb`)
- R Jupyter notebook plotting count Venn diagrams for the hits per mining pipeline (`./Visualisation/Mining Pipeline Venn.ipynb`)
