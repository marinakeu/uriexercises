'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular".
Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem
correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
Mostre a respectiva mensagem após a validação dos valores.
'''
import math

a, b, c = [float(item) for item in input().split()]
delta = (b ** 2) - (4 * a * c)

if a == 0 or delta < 0:
  print("Impossivel calcular")
else:
    delta = math.sqrt(delta)
    print("R1 = {:.5f}".format((- b + delta) / (2 * a)))
    print("R2 = {:.5f}".format((- b - delta) / (2 * a)))
