from math import *
from decimal import *
class dicotomia():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.d = self.kalc(self.a,self.b,self.c)
        self.result = self.dic(self.a,self.b,self.c,self.d)
    def form(self,x):
        return Decimal(3*(x**3)-4)
    def dic(self,a,b,c,d):
        m=(Decimal(a)+Decimal(b))/Decimal(2)
        fm=self.form(Decimal(m))
        fa=self.form(Decimal(a))
        fb=self.form(Decimal(b))
        if(fabs(b-a)<=c and fm<=c and d<=0):
            return[Decimal(m),Decimal(fabs(b-a)/2)]
        d=d-1
        if(fa*fm<0):
            return self.dic(a,m,c,d)
        else:
            return self.dic(m,b,c,d)
    def kalc(self,a,b,c):
        k=(log10(fabs(b-a))-log10(c))/log10(2)
        return ceil(k)
    def getresult(self):
        return self.result
re = dicotomia(0,2,0.03)
r = re.getresult()
print ("Resultado: ", r[0], " ± ", r[1])