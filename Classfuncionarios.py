class Funcionario():

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario



    def aumentar_salario(self, valor):
        percent = valor / 100
        valor = self.salario * percent
        self.salario = valor + self.salario
        return self.salario

