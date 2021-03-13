# programa 4.9 - pagamento pelo fornecimento de energia eletrica
print("""
[R]= Residencial
[I]= Industrial
[C]= Comercio
""")
valor = 0
qntKWh = float(input('KWh consumidos? '))
tipoInstalacao = str(input('Tipo de instalação: [R][I][C]: ')).upper()

if tipoInstalacao == 'R':
    if qntKWh <= 500:
        valor = 0.40
    else:
        valor = 0.65
elif tipoInstalacao == 'C':
    if qntKWh <= 1000:
        valor = 0.55
    else:
        valor = 0.60
elif tipoInstalacao == 'I':
    if qntKWh <= 5000:
        valor = 0.55
    else:
        valor = 0.60
else:
    print('Digite uma opção válida!')
print(f'O valor de sua fatura foi de R${qntKWh* valor:6.2f} Reais.')
