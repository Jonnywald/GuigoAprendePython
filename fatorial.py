
def fatorial(numero):
	
	if numero == 0:
		return 1
	else:
		resultado = numero * fatorial(numero-1)
	return resultado
