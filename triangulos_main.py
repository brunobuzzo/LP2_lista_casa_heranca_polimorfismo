from Classtriangulos import Triangulo


triangulo = Triangulo()
cond = False
while cond == False:
    ladoA = int(input('Informe o valor do lado A: '))
    ladoB = int(input('Informe o valor do lado B: '))
    ladoC = int(input('Informe o valor do lado C: '))
    cond1 = triangulo.recebe_valor(ladoA, ladoB, ladoC)
    cond2 = triangulo.calcula_perimetro()
    if cond1 == False or cond2 == False:
        print('\nValores não compoem a existencia de um triangulo! Repita a operação!\n')
        cond = False
    else:
        cond = True

triangulo.retorna_perimetro()
        
triangulo.calcula_maior()

triangulo.retorna_maior()

