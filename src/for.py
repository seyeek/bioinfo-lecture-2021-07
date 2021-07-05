import sys

if len(sys.argv) !=2:
    print(f"usage: python {sts.argv[0]} [n1]")
    sys.exit()
x=int(sys.argv[1])
val=1
for i in range(1,x+1) :
    val*=i
print(val)
