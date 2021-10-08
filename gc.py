import argparse

parser = argparse.ArgumentParser(
    description="This programn calculates the gc content of a string of DNA")
parser.add_argument('-i', help="The FASTA file")
args = parser.parse_args()


def gccontent(seq):
    return round(
        ((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)


with open(args.i, 'r') as f:
    fasta = [l.strip() for l in f.readlines()]


fastadic = {}
fastalaber = ''
for line in fasta:
    if '>' in line:
        fastalabel = line
        fastadic[fastalabel] = ''
    else:
        fastadic[fastalabel] += line

resultdic = {key: gccontent(value) for (key, value) in fastadic.items()}
maxgckey = max(resultdic, key=resultdic.get)
print(f'{maxgckey[1:]}\n{resultdic[maxgckey]}')
