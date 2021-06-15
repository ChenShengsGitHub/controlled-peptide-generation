

def modi(path):
    peptide = ''
    with open(path.replace('.fasta', '_|1-80.txt'), 'w') as new_file:
        for line in open(path).readlines():
            if line.startswith('>'):
                if 1 <= len(peptide) <= 80:
                    new_file.write(peptide + '\n')
            else:
                peptide += line.strip()


modi('~/data/uniprot/uniprot-reviewed_no.fasta')
modi('~/data/uniprot/uniprot-reviewed_yes.fasta')
