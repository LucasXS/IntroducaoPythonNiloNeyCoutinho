# Programa 4.7 - Categoria x produtos usando o ELIF!
categoria = int(input('Digite a categoria do produto: '))
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
elif categoria == 5:
    preco = 31
else:
    preco = 0
    print('Categoria invalida! Digite um valor entre 1 e 5.')
print(f'O produto {categoria} custa R${preco:6.2f} Reais')