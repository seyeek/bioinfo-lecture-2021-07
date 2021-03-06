counpss = 0
counchrom = 0

with open("070.vcf", "r") as data:
    for line in data:
        if line.startswith("#"):
            pass
        else:
            counchrom += 1
            erow = line.strip().split("\t")
            if erow[6] == "PASS":
                counpss += 1
            else:
                continue

print("chr21 is", counchrom)
print("pass filter is", counpss)

# ---
# teacher

cnt_all = 0
cnt_pass = 0

with open("070.vcf", "r") as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            header = line
            filter_idx = header.index("FILTER")
        data = line.strip().split("\t")
        cnt_all += 1
        if data[filter_idx] == "PASS":
            cnt_pass += 1

print(cnt_pass, cnt_all, cnt_pass / cnt_all)
