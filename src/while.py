import sys

if len(sys.argv) !=2:
    print(f"usage: python (sys.argv[0]) [n1]")
    sys.exit()

x=1
i=1
while  i<=int(sys.argv[1]):
    x*=i
    i+=1

print(x)
