# INTRODUÇÃO À PROGRAMAÇÃO COM PYTHON
# Exer 3.15 do livro do projeto Nilo Ney Coutinho Menezes

qnt_km_percorridos = float(input('Quantos KM você percorreu? '))
qnt_dias_alugados = int(input('Quantos dias alugados? '))
valor_a_pagar = qnt_km_percorridos * 0.15 + qnt_dias_alugados * 60
print('Você irá pagar R${:.2f} por {} dias de carro alugado!'.format(valor_a_pagar, qnt_dias_alugados))
