import sys


with open ("hahaha.txt",'r') as handle:
    data = handle.readlines()

print(data)



try:
    with open("hahaha.txt",'r') as handle:
        data=handle.readlines()
except FileNotFoundError as err :
    print("νμΌμμ")
    sys.exit()

print(data)
