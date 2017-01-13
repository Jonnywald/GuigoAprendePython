from fatorial import fatorial
def const_e():
	n = fatorial(50)
	e = (1+(1/n))**n
	return e
#abaixo: calculo do numero PI pelo serie de Nilakantha.
def const_Pi():
	pi = 3
	cont = 0
	sinal = 1
	div1 = 2
	div2 = 3
	div4 = 4
	while(cont < 100){
		cont += 1
		pi += (4/(div1*div2*div3))*sinal
		sinal *= -1
		div1 += 2
		div2 += 2
		div3 += 2
	}
	return pi