'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''

a, b, c =  [int(item) for item in input().split()]
list = [a, b, c]
list.sort()

print(list[0], list[1], list[2],"" ,a, b, c, sep="\n")