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
	return e
#abaixo: calculo do numero PI pela serie de Nilakantha.
def const_Pi():
	pi = Decimal(3)
	cont = 0
	sinal = 1
	div1 = 2
	div2 = 3
	div3 = 4
	while(cont < 10000):
		cont += 1
		pi += (Decimal(4)/(Decimal(div1)*Decimal(div2)*Decimal(div3)))*sinal
		sinal *= -1
		div1 += 2
		div2 += 2
		div3 += 2
	return pi
	
print (const_Pi())
#print (const_e())
