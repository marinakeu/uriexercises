'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo
necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha,
caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''
value = int(input())
leftover = value
result = []

for bill in (100, 50, 20, 10, 5, 2, 1):
  decomposition = leftover // bill
  leftover -= (decomposition * bill)
  result.append(decomposition)

print(value, '{} nota(s) de R$ 100,00'.format(result[0]),
'{} nota(s) de R$ 50,00'.format(result[1]),
'{} nota(s) de R$ 20,00'.format(result[2]),
'{} nota(s) de R$ 10,00'.format(result[3]),
'{} nota(s) de R$ 5,00'.format(result[4]),
'{} nota(s) de R$ 2,00'.format(result[5]),
'{} nota(s) de R$ 1,00'.format(result[6]), sep='\n')