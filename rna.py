import argparse

parser = argparse.ArgumentParser(
    description="This programn transcribe a strand of dna")
parser.add_argument('-i', help="The FASTA file")
args = parser.parse_args()

with open(args.i, 'r') as r:
    content = r.read()
    content = content.replace('T', 'U')
print(content)
