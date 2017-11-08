class Triangulo():

    def __init__(self):
        self.ladoA = 0
        self.ladoB = 0
        self.ladoC = 0
        self.perimetro = 0
        self.ladoM = 0
        self.maior = ''

    def recebe_valor(self, ladoA, ladoB, ladoC):
        if ladoA > 0 and ladoB > 0 and ladoC > 0:
            self.ladoA = ladoA
            self.ladoB = ladoB
            self.ladoC = ladoC
            return True
        return False


    def calcula_perimetro(self):
        if (abs(self.ladoA - self.ladoB) < self.ladoC) == True and (self.ladoC < (self.ladoA + self.ladoB)) == True:
            self.perimetro = self.ladoA + self.ladoB + self.ladoC
         
            return self.perimetro
        elif (abs(self.ladoB - self.ladoC) < self.ladoA) == True and (self.ladoA < (self.ladoB + self.ladoC)) == True:
            self.perimetro = self.ladoA + self.ladoB + self.ladoC
  
            return self.perimetro
        elif (abs(self.ladoC - self.ladoA) < self.ladoB) == True and (self.ladoB < (self.ladoC + self.ladoA)) == True:
            self.perimetro = self.ladoA + self.ladoB + self.ladoC

            return self.perimetro
        return False

    def calcula_maior(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            self.ladoM = self.ladoA
            self.maior = 'lado A'
            return True
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            self.ladoM = self.ladoB
            self.maior = 'lado B'
            return True
        elif self.ladoC > self.ladoB and self.ladoC > self.ladoA:
            self.ladoM = self.ladoC
            self.maior = 'lado C'
            return True
        return False

    def retorna_maior(self):
        print('O ',self.maior ,' é o maior lado com o valor de ', self.ladoM)

    def retorna_perimetro(self):
        print('O perimetro do triangulo é: ', self.perimetro)
        
        
