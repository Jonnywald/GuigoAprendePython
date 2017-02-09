#fatorial
#arquivo feito por Guilherme Del Rio
#abaixo: calculo de fatorial pela propria definicao
from decimal import *
def fatorial(numero):
	
	if numero == 0:
		return Decimal(1)
	else:
		resultado = Decimal(numero) * Decimal(fatorial(Decimal(numero)-Decimal(1)))
	return Decimal(resultado)
