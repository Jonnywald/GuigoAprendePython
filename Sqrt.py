#raiz quadrada
#arquivo feito por Guilherme Del Rio
#abaixo: calculo de raiz quadrada pelo metodo babilônico
def raizQuadrada (numero):
	chute = 1
	cont = 0
	while (((numero/chute)!=chute) and (cont < 100)):
		chute = ((numero/chute)+chute)/2
		cont += 1
	return chute
