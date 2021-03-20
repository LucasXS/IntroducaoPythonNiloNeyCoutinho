# Programa 4.3 - Cálculo de Imposto de Renda
"""
    Exemplo importante:
    Salario 5.000
    3000 * 20% + 2000 (resto) * 35%
"""
salario = float(input('Digite seu sálario: '))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
    base = 1000
print(f'Salário:  R${salario:6.2F}\nImposto a pagar {imposto:6.2f}')
