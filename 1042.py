'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''

a, b, c =  [int(item) for item in input().split()]
sorted_itens = [a, b, c]
sorted_itens.sort()

print(sorted_itens[0], sorted_itens[1], sorted_itens[2],"" ,a, b, c, sep="\n")