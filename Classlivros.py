class Livro():


    def __init__(self):
        self.nome = 'Introdução à programação com Python'
        self.qtd_paginas = 334
        self.autor = 'Nilo Ney Coutinho Menezes'
        self.preco = 55.90


    def getPreco(self):
        return self.preco


    def setPreco(self,valor):
        if type(valor) == float:
            self.preco = valor
        elif type(valor) == int:
            self.preco = float(valor)
        return self.preco        


