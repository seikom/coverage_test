### script to report a list of genes with less than 30x at coverage

### Date: 2021/03
### authour: Seiko Makino
### usage: list_genes_cov30.py <sambamba_output>

import os
import sys
import argsparse

### parse a argument
parser = argparse.ArgumentParser(description='Report a list of genes with less than 100% at coverage 30x')
parser.add_argument('--file', '-f', help='sambamba output file for coverage analysis')
args = parser.parse_args()

file=args.file

### read in a sambamba output file

f = open(file,'r')
print(f.readline(1))


### identify rows with less than 100% at cov30

### create a list of genes

### write a report as a text file
