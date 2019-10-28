'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa
um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis
no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de
notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial,
conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
'''
value = float(input()) +  0.001
leftover = value
bill_result = []
coin_result = []

for bill in (100, 50, 20, 10, 5, 2):
    decomposition = leftover // bill
    leftover -= (decomposition * bill)
    bill_result.append(decomposition)

for coin in (1, 0.50, 0.25, 0.10, 0.05, 0.01):
    decomposition = leftover // coin
    leftover -= (decomposition * coin)
    coin_result.append(decomposition)

print(
    "NOTAS:",
    '{:.0f} nota(s) de R$ 100.00'.format(bill_result[0]),
    '{:.0f} nota(s) de R$ 50.00'.format(bill_result[1]),
    '{:.0f} nota(s) de R$ 20.00'.format(bill_result[2]),
    '{:.0f} nota(s) de R$ 10.00'.format(bill_result[3]),
    '{:.0f} nota(s) de R$ 5.00'.format(bill_result[4]),
    '{:.0f} nota(s) de R$ 2.00'.format(bill_result[5]),
    "MOEDAS:",
    '{:.0f} moeda(s) de R$ 1.00'.format(coin_result[0]),
    '{:.0f} moeda(s) de R$ 0.50'.format(coin_result[1]),
    '{:.0f} moeda(s) de R$ 0.25'.format(coin_result[2]),
    '{:.0f} moeda(s) de R$ 0.10'.format(coin_result[3]),
    '{:.0f} moeda(s) de R$ 0.05'.format(coin_result[4]),
    '{:.0f} moeda(s) de R$ 0.01'.format(coin_result[5]),
    sep='\n')
