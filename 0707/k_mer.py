import sys

nmer = int(sys.argv[1])
base = ["A", "T", "G", "C"]


def kmer(nmer):
    new_base = []
    if nmer < 1:
        return new_base
    new_base = list(kmer(nmer - 1))
    new_base.extend(base)
    new_base.sort()
    return new_base


print(kmer(nmer))
