from Classtriangulos import Triangulo


tr = Triangulo()

cond = False
while cond == False:
    tr.ladoA = int(input('Informe o tamanho do lado A: '))
    tr.ladoB = int(input('Informe o tamanho do lado B: '))
    tr.ladoC = int(input('Informe o tamanho do lado C: '))    
    if (abs(tr.ladoA - tr.ladoB) < tr.ladoC) == True and (tr.ladoC < (tr.ladoA + tr.ladoB)) == True:
        area = tr.calc_perimetro()
        cond = True
    elif (abs(tr.ladoB - tr.ladoC) < tr.ladoA) == True and (tr.ladoA < (tr.ladoB + tr.ladoC)) == True:
        area = tr.calc_perimetro()
        cond = True
    elif (abs(tr.ladoC - tr.ladoA) < tr.ladoB) == True and (tr.ladoB < (tr.ladoC + tr.ladoA)) == True:
        area = tr.calc_perimetro()
        cond = True
    else:
        print('Os valores digitados não compoem um triangulo!\n Refaça a operação...')
        cond = False


maior = tr.calc_maior()

print('A área do triangulo é de ',area,'. E o ',maior,' é o maior lado do triagulo')

