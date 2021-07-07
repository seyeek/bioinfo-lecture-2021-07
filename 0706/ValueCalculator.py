class ValueCalculator:
    def __init__(self,val:str):
        self.val = val

    def __add__ (self,other):
        return self.val + other.val

if __name__ == "__main__":      #python으로만 실행할때 실행되것
                            #불러진 파일로 실행될때는 main이 아니기 때문에 실행안됨
    print('hi')

