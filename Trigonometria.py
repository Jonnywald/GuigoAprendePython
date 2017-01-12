from fatorial import fatorial
from Sqrt import raizQuadrada
def seno(numero):
	resultado = raizQuadrada(1 - (coseno(numero))**2)
	return resultado
def coseno(numero):
	cont = 0
	resultado = 0
	while(cont < 50):
		cont += 1
		resultado += (((-1)**cont)*(numero**(2 * cont)))/(fatorial(2 * cont))
	return resultado

val1 = seno(0.52359877559)
val2 = coseno(1.0471975512)

print (val1)
print (val2)