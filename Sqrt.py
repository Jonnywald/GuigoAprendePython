def raizQuadrada (numero):
	chute = 1
	cont = 0
	while (((numero/chute)!=chute) and (cont < 100)):
		chute = ((numero/chute)+chute)/2
		cont += 1
	return chute
