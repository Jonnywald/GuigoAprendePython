#constantes matematicas
#aquivo feito por Guilherme Del Rio
from fatorial import fatorial
#abaixo: calculo do numero de euler com base na sua definição como limite tendendo ao infinito
#aproximação utilizando 50!(cinquenta fatorial)
def const_e():
	n = fatorial(12)
	#print (n)
	e = (1+(1/n))**n
	return e
#abaixo: calculo do numero PI pela serie de Nilakantha.
def const_Pi():
	pi = 3
	cont = 0
	sinal = 1
	div1 = 2
	div2 = 3
	div3 = 4
	while(cont < 10000):
		cont += 1
		pi += (4/(div1*div2*div3))*sinal
		sinal *= -1
		div1 += 2
		div2 += 2
		div3 += 2
	return pi
	
#print (const_Pi())
#print (const_e())