class Triangulo():

    def __init__(self):
        self.ladoA = 0
        self.ladoB = 0
        self.ladoC = 0

    def calc_perimetro(self):
        lista = [self.ladoA, self.ladoB, self.ladoC]
        return sum(lista)
            
    def calc_maior(self):
        dic = {'lado A': self.ladoA, 'lado B': self.ladoB, 'lado C': self.ladoC}
        return max(dic)
        
        
