file_name = "covid19.fasta"

data = dict()   #data={}로 딕셔너리 만들어도 됨

with open(file_name, 'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] += 1

print(data)
