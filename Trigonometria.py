from fatorial import fatorial
from Sqrt import raizQuadrada
from constantes import *
#abaixo: converção de graus para radianos
def converterGrausParaRad(numero):
	rad = (numero/180)*const_Pi()
	return rad
#abaixo: definição da função seno por sin² + cos² = 1
def seno(numero):
	resultado = 0
	resultado = raizQuadrada(1 - (coseno(numero))**2)
	return round(resultado,10)
#abaixo:definição da função coseno pela sua expanção da serie de taylor 
def coseno(rad):
	numero = converterGrausParaRad(rad)
	cont = 0
	resultado = 1
	while(cont < 50):
		cont += 1
		resultado += (((-1)**cont)*(numero**(2 * cont)))/(fatorial(2 * cont))
	return round(resultado,10)
#abaixo: definição da função tangente pela propria definição
def tangente(numero):
	resultado = 0
	resultado = (seno(numero))/(coseno(numero))
	return resultado
#abaixo: definição da função cotangente pela propria definição
def cotangente(numero):
	resultado = 0
	resultado = (coseno(numero))/(seno(numero))
	return resultado
#abaixo: definição da função secante pela propria definição
def secante(numero):
	resultado = 0
	resultado = 1/(coseno(numero))
	return resultado
	#abaixo: definição da função cosecante pela propria definição
def cosecante(numero):
	resultado = 0
	resultado = 1/(seno(numero))
	return resultado
	
val1 = seno(30)
val2 = coseno(60)
print (val1)
print (val2)
