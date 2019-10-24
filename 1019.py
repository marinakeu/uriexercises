'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento
em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para
horas:minutos:segundos, conforme exemplo fornecido.
'''
total_seconds = int(input())
leftover = total_seconds
result = []

for unit in (3600, 60, 1):
  decomposition = leftover // unit
  leftover -= (decomposition * unit)
  result.append(decomposition)

print(result[0], result[1], result[2], sep=':')