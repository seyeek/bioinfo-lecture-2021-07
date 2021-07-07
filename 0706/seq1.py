
Seq1 = "AGTTATAG"

print(Seq1[3:6])
print(len(Seq1))

Seq2 = "ATGttATaG"
US=Seq2.upper()
LS=Seq2.lower()

print(US)
print(LS)


Seq3= "ATGTTTATAG"

for i in range(0,8,3):
    print(Seq3[i:i+3])

rSeq3=Seq3[::-1]
print(rSeq3)

print("pro 028")

se={'A':'T','C':'G','G':'C','T':'A'}
coupSeq3=[]

for i in range(0,len(Seq3)):
    a=Seq3[i]
    coupSeq3.append(se[a])
print(str(coupSeq3))

#강사님
comp=""
for s in Seq3 :
    comp+=se[s]
print(comp)

#30
import re
print("30")

Seq3="AGTTTATAG"

for i in range(len(Seq3)):
    s=Seq3[i:i+2]
    if s=="TT":
        print(i)

#31
print("from 31 list")
s="AA,AC,AG,AT"
data = s.split(",")
print(data)
data.append("CA")
print(data)
print(data[::-1])

data=[3, 1, 1, 2, 0, 0, 2, 3, 3]
print(min(data))
print(max(data))

dic={}
for i in data:
    if i in dic:
        dic[i] +=1
    else:
        dic[i]=1
print("times of num appear",dic)


