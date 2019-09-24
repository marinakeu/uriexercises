'''
Faça um programa que leia três valores e apresente o maior
dos três valores lidos seguido da mensagem “eh o maior”.
Utilize a fórmula: MaiorAB = (a+b+abs(a-b))/2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço
e a mensagem "eh o maior".
'''

input = input().split()

a = int(input[0])
b = int(input[1])
c = int(input[2])

maior_ab = (a + b + abs(a-b))/2
maior = int((c + maior_ab + abs(c - maior_ab))/2)

print("{} eh o maior".format(maior))