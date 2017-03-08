#estatistica
#arquivo feito por guilherme del rio
from math import *
class dados_continuos():
	dados = (())
	def __init__ (self, *agrs):
		dados=(args)
	def add_data(data_range, data):
		dados
def media_aritimetica(dados):
    for x in dados:
        soma += x
    return (soma/len(dados))
def media_ponderada(dados):
    for x in dados:
        soma +=( x[0] * x[1])
        p += x[1]
    return (soma/p)
def media_geometrica(dados):
    for x in dados:
        soma += x
    return (root(len(dados),soma))
def media_harmonica(dados):
    for x in dados:
        soma += x**-1
    return (len(dados)/soma)
