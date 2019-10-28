'''
Você deve fazer um programa que leia um valor qualquer e
apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75],
(75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos,
deverá ser impressa a mensagem “Fora de intervalo”.

O símbolo ( representa "maior que". Por exemplo:
[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

Entrada
O arquivo de entrada contém um número com ponto flutuante qualquer.

Saída
A saída deve ser uma mensagem conforme exemplo abaixo.
'''
entrada = float(input())
intervalos = ((0, 25, "[0,25]"), (25.01, 50, "(25,50]"),
(50.01, 75, "(50,75]"), (75.01, 100, "(75,100]"))
saida = "Fora de intervalo"

for intervalo in intervalos:
  if entrada >= intervalo[0] and entrada <= intervalo[1]:
    saida = "Intervalo {}".format(intervalo[2])

print(saida)
