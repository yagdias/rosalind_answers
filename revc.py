import argparse

parser = argparse.ArgumentParser(
    description='This progranm writes a complementar string of dna')
parser.add_argument('-i', help="The input file")
args = parser.parse_args()


new = ' '
dna = str(input())
dna = dna
for n in dna:
    print(n)
    if n == 'A':
        new += 'T'
    elif n == 'C':
        new += 'G'
    elif n == 'G':
        new += 'C'
    elif n == 'T':
        new += 'A'


def reverse(x):
    return x[::-1]


new = reverse(new)
print(new)
