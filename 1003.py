'''
Leia dois valores inteiros, no caso para variáveis A e B.
A seguir, calcule a soma entre elas e atribua à variável SOMA.
A seguir escrever o valor desta variável.

Entrada
O arquivo de entrada contém 2 valores inteiros.

Saída
Imprima a variável SOMA com todas as letras maiúsculas,
com um espaço em branco antes e depois da igualdade seguido
pelo valor correspondente à soma de A e B.
'''

a = input()
b = input()

soma = int(a) + int(b)

print("SOMA = {}".format(soma))