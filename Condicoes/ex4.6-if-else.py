# Programa 4.6 - Categoria x produtos usando o if e else!
categoria = int(input('Digite a categoria do produto: '))
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else:
                if categoria == 5:
                    preco = 31
                else:
                    preco = 0
                    print('Categoria invalida! Digite um valor entre 1 e 5.')
print(f'O produto {categoria} custa R${preco:6.2f} Reais')