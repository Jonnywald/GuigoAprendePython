from math import *
from decimal import *
class dicotomia():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.d = self.kalc(self.a,self.b,self.c)
        self.result = self.dic(self.a,self.b,self.c,self.d)
    def form(self,x):
        return Decimal(3*(x**3)-4)
    def dic(self,a,b,c,d):
        m=(Decimal(a)+Decimal(b))/Decimal(2)
        fm=self.form(Decimal(m))
        fa=self.form(Decimal(a))
        fb=self.form(Decimal(b))
        if(fabs(b-a)<=c and fm<=c and d<=0):
            return[Decimal(m),Decimal(fabs(b-a)/2)]
        d=d-1
        if(fa*fm<0):
            return self.dic(a,m,c,d)
        else:
            return self.dic(m,b,c,d)
    def kalc(self,a,b,c):
        k=(log10(fabs(b-a))-log10(c))/log10(2)
        return ceil(k)
    def getresult(self):
        return self.result
class interpo_lagrange():
    #metodo construtor (inicializa as variaveis)
    def __init__(self):
        self.x = [];
        self.saida = Decimal(0);
        self.entrada = None;
    #adiciona um ponto(x e y) para a lista de pontos
    def add_ponto(self,x,fx):
        tupla = (x,fx);
        self.x.append(tupla);
    #seta uma valor para se calcular
    def set_entrada(self,val):
        self.entrada = Decimal(val);
    #calculo do resultado da interpolacao pelo metodo de lagrange
    def calc_saida(self):
        #checa se foi setado um valor para se calcular
        if (not(self.entrada is None)):
            #checa se tem o numero necessario de pontos para iniciar a interpolacao
            if (len(self.x)>1):
                #variaveis para o inicio da lista de pontos
                a = 0;
                b = 0;
                #variavel para o somatório
                soma = 0;
                while(a<len(self.x)):
                    #variavel para o produtorio sempre se reinicializando
                    prod = 1;
                    while(b<len(self.x)):
                        #desconsiderando valores iguais com o intuido de não geral uma indeterminação matematica (divisao por zero)
                        if (a!=b):
                            #calculo do produtorio (ja com um valor setado) pelo metodo de lagrange para o polinomio
                            prod *= Decimal(Decimal(self.entrada-self.x[b][0])/Decimal(self.x[a][0]-self.x[b][0]));
                        b += 1;
                    #calculo do polinomio com um valor ja setado
                    soma += Decimal(prod)*Decimal(self.x[a][1])
                    a += 1;
                #atribuicao do valor para o atributo do objeto
                self.saida = soma;
            else:
                #caso nao haja pontos o suficiente para realizar a intepolacao é exibida a mensagem abaixo
                print('Erro! adicione mais pontos!');
        else:
            #caso nao haja um valor inicial para realizar a intepolacao é exibida a mensagem abaixo
            print('Erro! adicione uma entrada!');
    #retorna o resultado da interpolacao
    def get_saida(self):
        return self.saida

re = dicotomia(0,2,0.03)
r = re.getresult()
print ("Resultado: ", r[0], " ± ", r[1])

var = interpo_lagrange()
var.set_entrada(0)
var.add_ponto(0,5)
var.add_ponto(3,14)
var.add_ponto(5,6)
var.calc_saida()
print ('Resultado: ',var.get_saida())
