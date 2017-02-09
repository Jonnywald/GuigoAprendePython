#raiz quadrada
#arquivo feito por Guilherme Del Rio
#abaixo: calculo de raiz quadrada pelo metodo babilônico
from decimal import *
def raizQuadrada (numero):
	chute = Decimal(1)
	cont = Decimal(0)
	while (((numero/chute)!=chute) and (cont < 100)):
		chute = Decimal(((numero/chute)+chute))/Decimal(2)
		cont += Decimal(1)
	return Decimal(chute)
