import sys

#try:
#    val = int(input("Enter: "))
#except ValueError as err:
#    print(err)
#    sys.exit()

#try:
#    print(10/val)
#except ZeroDivisionError as err:
#    print(err)
#    sys.exit()
#_______________________________
try:
    val = int(input("Enter: "))
    print(10/val)
except ZeroDivisionError as err:
    print(err)
    sys.exit()
except ValueError as err2:
    print(err2)
    sys.exit()

