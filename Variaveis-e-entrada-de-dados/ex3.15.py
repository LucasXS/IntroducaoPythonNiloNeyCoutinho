# INTRODUÇÃO À PROGRAMAÇÃO COM PYTHON
# Exer 3.15 do livro do projeto Nilo Ney Coutinho Menezes

cigarros_por_dia = int(input('Quantos cigarros você fuma por dia? '))
anos_fumando = int(input('Há quantos anos você fuma? '))
reducao_vida_minutos = cigarros_por_dia * 10 * anos_fumando * 365
# dia tem 24 horas e cada hora 60 minutos
reducao_vida_dias = reducao_vida_minutos / (24 * 60)
print('Você já perdeu {:.2f} dias de vida! '.format(reducao_vida_dias))