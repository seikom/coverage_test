#  How to run list_genes_under_cov30.py  

## Description  
list_genes_under_cov30.py is a script to identify and create a report csv file with genes with suboptimal coverage at 30x from a sambamba output file. 

## Installation   
Install the packages in requirements.txt before running the script. 

```bash
pip install -r requirements.txt 
```

The script is developed and tested in python 3.6.10 environment.

## Usage  
A sambamba output file with appropriate headers is required to run the script:
```bash
python list_genes_under_cov30.py -v --file/-f /<NGS_run_name.sambamba_output.txt/>
```

The input file must be separated in tab delimiter.

Header must be in this format: 
```bash
#chromosome	StartPosition	EndPosition	FullPosition	NotUsed	NotUsedGeneSymbol;Accession	Size	readCount	meanCoverage	percentage30	sampleName
```

Example:
```bash 
python list_genes_under_cov30.py -v -f NGS148_34_139558_CB_CMCMD_S33_R1_001.sambamba_output.txt
```

Use '--help/-h' option to print the help:
```bash
python list_genes_under_cov30.py --help/-h
```

The output file is generated as a csv format with the NGS run name from the input file (e.g. NGS_run_name.report_under30x.csv, NGS148_34_139558_CB_CMCMD_S33_R1_001.report_under30x.csv)

## Author  
Seiko Makino (seiko.makino@nhs.net)

## Version history  
v0.0.1 Initial commit

