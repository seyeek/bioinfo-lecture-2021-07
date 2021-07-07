import sys

cnt = int(sys.argv[1])

base = {0: 0, 1: 1}


def fir(cnt):
    if cnt == 0:
        return 0
    elif cnt == 1:
        return 1
    elif cnt >= 2:
        return fir(cnt - 1) + fir(cnt - 2)


print(fir(cnt))
