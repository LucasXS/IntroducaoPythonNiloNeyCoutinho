# Programa 4.3 - Conta de telefone com três faixas de preço!
valorMinutos = int(input('Quantos minutos foram usados este mês? '))
minuto = valorMinutos
preco = 0

if minuto < 200:
   preco = minuto * 0.20
else:
    if minuto < 400:
        preco = minuto * 0.18
    else:
        preco = minuto * 0.15
print(f'Você irá pagar R${preco:6.2f} Reais este mês')