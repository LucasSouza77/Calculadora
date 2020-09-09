
def calculate():
    operação = input('''
Digite a operação matemática que você deseja :
(+) ADIÇÃO 
(- ) SUBTRAÇÃO 
(* )MULTIPLICAÇÃO
(/ )DIVISÃO 
''')

    nu1 = float(input('ensira o primero valor: '))
    nu2 = float(input('insira o segundo valos: '))
# ADIÇAO
    if operação == '+':
        print('{} + {} = '.format(nu1, nu2))
        print(nu1 + nu2)
# SUBTRAÇAO
    elif  operação == '-':
        print('{} - {} = '.format(nu1, nu2))
        print(nu1 - nu2)
# MULTIPLICAÇÃO
    elif operação == '*':
        print('{} * {} = '.format(nu1, nu2))
        print(nu1 * nu2)
# DIVISAO
    elif operação== '/':
        print('{} / {} = '.format(nu1, nu2))
        print(nu1 / nu2)
# ERRO
    else:
        print('.Você não digitou um operador válido, execute o programa novamente. ')

    # Add again() function to calculate() function
    again()

def again():
    calcular_novamente = input('''
Deseja calcular novamente?
Digite S para SIM ou N para NÃO.
''')

    if calcular_novamente.upper() == 'S':
        calculate()
    elif calcular_novamente.upper() == 'N':
        print('ATÉ PRÓXIMA.')
    else:
        again()

calculate()
