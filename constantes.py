#constantes matematicas
#aquivo feito por Guilherme Del Rio
from fatorial import fatorial
from decimal import *
getcontext().prec = 30
#abaixo calculo do numero de euler com base na sua definicao como limite tendendo ao infinito
#aproximacao utilizando 50!(cinquenta fatorial)
def const_e():
	n = fatorial(20)
	#print (n)
	e = (Decimal(1)+(Decimal(1)/Decimal(n)))**Decimal(n)
	return Decimal(e)
#abaixo: calculo do numero PI pela serie de Nilakantha.
def const_Pi():
	pi = Decimal(3)
	cont = Decimal(0)
	sinal = Decimal(1)
	div1 = Decimal(2)
	div2 = Decimal(3)
	div3 = Decimal(4)
	while(cont < 10000):
		cont += Decimal(1)
		pi += (Decimal(4)/(Decimal(div1)*Decimal(div2)*Decimal(div3)))*sinal
		sinal *= Decimal(-1)
		div1 += Decimal(2)
		div2 += Decimal(2)
		div3 += Decimal(2)
	return Decimal(pi)
	
print (const_Pi())
#print (const_e())
