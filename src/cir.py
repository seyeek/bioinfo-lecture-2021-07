#!/usr/bin/python
#r=input("radius?")
#r=float(r)

from math import pi

#ans=r*r*(pi)
#print(ans)

import sys
if len(sys.argv) != 2:
    print(f"#usger: python {sys.argv[0]} [nmu]")
    sys.exit()

r =int(sys.argv[1])
result = round(r**2*pi,2)   #round로 소수점 두번째자리 까지
print(result)
