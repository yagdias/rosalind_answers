import argparse

parser = argparse.ArgumentParser(
    description="This programn counts each nucleotide in a single fasta")
parser.add_argument('-i', help="The FASTA file")
args = parser.parse_args()

adenine = thymine = guanine = cytosine = 0
with open(args.i, 'r') as rosa:
    rosa_cont = rosa.read()
    for nucleotide in rosa_cont:
        if nucleotide == 'A':
            adenine += 1
        if nucleotide == 'T':
            thymine += 1
        if nucleotide == 'G':
            guanine += 1
        if nucleotide == 'C':
            cytosine += 1
print(adenine, cytosine, guanine, thymine)
