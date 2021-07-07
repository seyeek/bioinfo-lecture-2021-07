class  A:
    def _int_(self):
        self.val=vla
    def _add_(self,other)
	return self.val +other.val
    def _mul_(self,other)
        return"_mul_"


a1=A("a") #A.val=a
a2=A("b")
print(a1.val + a2.val)
print(a1+a2) #_add_ 가 있기 때문에
print(a1*a2) #_mul_


:wq
