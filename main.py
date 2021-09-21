# 1- import - bibliotecas
# 2 - class
# 3 - definition = métodos e funções

def print_hi(name):
    print(f'Oii, {name}')

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 // num2
    else:
        return 'Não dividirás por zero'


if __name__ == '__main__':
    print_hi('Sumida')

    resultado = somar(3,3)
    print(f'O resultado da soma é: {resultado} ')

    resultado = subtrair(13, 3)
    print(f'O resultado da subtração é: {resultado} ')

    resultado = multiplicar(6, 3)
    print(f'O resultado da multiplicação é: {resultado} ')

    resultado = dividir(9, 3)
    print(f'O resultado da divisão é: {resultado} ')

