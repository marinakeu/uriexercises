'''
Faça um programa que mostre os números pares entre 1 e 100, inclusive.

Entrada
Neste problema extremamente simples de repetição não há entrada.

Saída
Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.
'''

'''
Primeira resolução
for number in range(101):
  if number % 2 == 0 and number != 0:
    print(number)
'''

#Segunda resolução
for number in range(2, 101, 2):
  print(number)