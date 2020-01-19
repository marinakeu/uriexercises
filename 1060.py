'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos
 (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''

positive_numbers = []

for i in range(6):
  if float(input()) > 0:
    positive_numbers.append(i)

print("{:} valores positivos".format(len(positive_numbers)))