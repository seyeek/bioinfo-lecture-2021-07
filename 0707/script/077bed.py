chr = 0

with open("077.bed", "r") as data:

    for line in data:
        lis = line.split()
        len = int(lis[2]) - int(lis[1])
        chr += int(len)

print(chr)


# ----
# teacher

with open("077.bed", "r") as handle:
    for line in handle:
        data = line.strip().split("\t")
        chrom, start, end = data
        length = int(end) - int(start)
        result += length
print(result)
