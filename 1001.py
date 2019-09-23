'''
Leia 2 valores inteiros e armazene-os nas variáveis a e B.
Efetue a soma de A e B atribuindo o seu resultado na variável X.
Imprima X conforme exemplo apresentado abaixo.

Entrada
A entrada contém 2 valores inteiros.

Saída
Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X
e pelo final de linha. Cuide para que tenha um espaço antes e depois do sinal de
igualdade, conforme o exemplo abaixo.
'''

a = input()
b = input()

x = int(a) + int(b)

print("X = {}".format(x))