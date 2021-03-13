# Programa 4.8  - Calculadora Simples
num1 = float(input('Nº1: '))
operador = str(input('Operador [+] [-] [*] [/]: '))
num2 = float(input('Nº2: '))

if operador == '+':
    res = num1 + num2
elif operador == '-':
    res = num1 - num2
elif operador == '*':
    res = num1 * num2
elif operador == '/':
    res = num1 / num2
else:
    print('Operador invalido! Digite o operador correto!')
print(f'O resultado da operação foi {res:6.2f}')
