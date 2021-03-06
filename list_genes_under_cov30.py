### script to report a list of genes with less than 30x at coverage

### Date: 2021/03
### authour: Seiko Makino
### usage: list_genes_cov30.py <sambamba_output>
### python 3.6.10

import os
import sys
import magic
import argparse
import pandas

### parse a argument
parser = argparse.ArgumentParser(description='Report a list of genes with less than 100% at coverage 30x')
parser.add_argument('--verbosity', '-v', help='increase output verbosity ', action='store_true')
parser.add_argument('--file', '-f', help='sambamba output file for coverage report', type=str)
args = parser.parse_args()

filename = args.file
verbose = args.verbosity


## setting pandas print option
#pandas.set_option("display.max_rows", None, "display.max_columns", None)

### check the input file format
try:
    filetype = magic.from_file(filename, mime=True)
    #print(filetype)
    if filetype == 'text/plain':
        pass
    else:
        print(f'The file {filename} is not a text file. Check. ')
        exit(1)
except Exception as e:
    print(e)
    print('Some error occurred. Exiting. ')
    exit(1)

### read in a sambamba output file
#filename = 'NGS148_34_139558_CB_CMCMD_S33_R1_001.sambamba_output.txt'
#file = open(filename, 'r', encoding = 'utf-8')
try:
    with open(filename, 'r', encoding='utf-8') as file:
        if verbose:
            print(f'Reading in {filename} ')
        #print(file.readline())
        df = pandas.read_table(file, delimiter='\t', header=0, index_col=False, delim_whitespace=True)  # 0th line as a header, columns has tab detelimiter or white space
        #print(df)
        #print(df.columns)
        if 'percentage30' not in df.columns or 'GeneSymbol;Accession' not in df.columns:
            print(f'The file may be missing columns \"percentage30\" or \"GeneSymbol;Accession\". Check. ')
            exit(1)
        else:
            ### identify rows with less than 100% at cov30 and keep the gene names
            df_under30 = df[df['percentage30'] != 100.0]
            GeneSymbol_under30 = df_under30['GeneSymbol;Accession'].drop_duplicates()
            if df_under30.shape[0] == 0:
                print(f'No genes with less than 100% in coverage 30x. Empty report generated. ')
            else:
                if verbose:
                    print(f'Genes with less than 100% in coverage 30x: ')
                    for v in GeneSymbol_under30.values:
                        print(v)
    ### write a report as a text file
            samplename = filename.split('.')[0]
            reportfilename = samplename + '.report_under30x.csv'
            GeneSymbol_under30.to_csv(reportfilename, index=False)
except FileNotFoundError as fnf_error:
    print(fnf_error)
    exit(1)



'''

# select row
df.loc(0)

# get column names
df.columns

# select column by column name
df['#chromosome']


'''
