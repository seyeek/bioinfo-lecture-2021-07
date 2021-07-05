

def greet():
    print("Hellow, Bioinformatic")

greet()



def greet1(name):
    print(f"Hello,{name}")    #반환하는 것이 없는 것

def greet2(num: int)-> int:    #반환하는 것이 있음 (함수에 return이 있음)
    return num*2

greet()
ret1 = greet1("ken")
print(ret1)

ret2 =greet2(3)
print(ret2)


