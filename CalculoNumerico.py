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
class interpo_lagrange():
    def __init__(self,entrada):
        self.saida = Decimal(0)
        self.entrada = Decimal(entrada)
    def calc_grau1(self,x0,fx0,x1,fx1):
        l0 = (Decimal(self.entrada-x1)/Decimal(x0-x1))
        l1 = (Decimal(self.entrada-x0)/Decimal(x1-x0))
        px = Decimal(Decimal(l0)*Decimal(fx0))+Decimal(Decimal(l1)*Decimal(fx1))
        self.saida = Decimal(px)
    def calc_grau2(self,x0,fx0,x1,fx1,x2,fx2):
        l0 = (Decimal(self.entrada-x1)/Decimal(x0-x1))*(Decimal(self.entrada-x2)/Decimal(x0-x2))
        l1 = (Decimal(self.entrada-x0)/Decimal(x1-x0))*(Decimal(self.entrada-x2)/Decimal(x1-x2))
        l2 = (Decimal(self.entrada-x0)/Decimal(x2-x0))*(Decimal(self.entrada-x1)/Decimal(x2-x1))
        px = Decimal(Decimal(l0)*Decimal(fx0))+Decimal(Decimal(l1)*Decimal(fx1))+Decimal(Decimal(l2)*Decimal(fx2))
        self.saida = Decimal(px)
    def calc_grau3(self,x0,fx0,x1,fx1,x2,fx2,x3,fx3):
        l0 = (Decimal(self.entrada-x1)/Decimal(x0-x1))*(Decimal(self.entrada-x2)/Decimal(x0-x2))*(Decimal(self.entrada-x3)/Decimal(x0-x3))
        l1 = (Decimal(self.entrada-x0)/Decimal(x1-x0))*(Decimal(self.entrada-x2)/Decimal(x1-x2))*(Decimal(self.entrada-x3)/Decimal(x1-x3))
        l2 = (Decimal(self.entrada-x0)/Decimal(x2-x0))*(Decimal(self.entrada-x1)/Decimal(x2-x1))*(Decimal(self.entrada-x3)/Decimal(x2-x3))
        l3 = (Decimal(self.entrada-x0)/Decimal(x3-x0))*(Decimal(self.entrada-x1)/Decimal(x3-x1))*(Decimal(self.entrada-x2)/Decimal(x3-x2))
        px = Decimal(Decimal(l0)*Decimal(fx0))+Decimal(Decimal(l1)*Decimal(fx1))+Decimal(Decimal(l2)*Decimal(fx2))+Decimal(Decimal(l3)*Decimal(fx3))
        self.saida = Decimal(px)
    def getSaida(self):
        return self.saida

re = dicotomia(0,2,0.03)
r = re.getresult()
print ("Resultado: ", r[0], " ± ", r[1])

var = interpo_lagrange(2)
var.calc_grau2(0,5,3,14,5,6)
print (var.getSaida())
