'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos,
meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias.
Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias,
como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.
'''
total_days = int(input())
leftover = total_days
result = []

for unit in (365, 30, 1):
  decomposition = leftover // unit
  leftover -= (decomposition * unit)
  result.append(decomposition)

print('{} ano(s)'.format(result[0]),
'{} mes(es)'.format(result[1]),
'{} dia(s)'.format(result[2]), sep='\n')