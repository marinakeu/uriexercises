'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1,
o valor unitário de cada peça 1, o código de uma peça 2, o número de
peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor
a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha
haverá 3 valores, respectivamente dois inteiros e um valor com 2
casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo,
lembrando de deixar um espaço após os dois pontos e um espaço após
o "R$". O valor deverá ser apresentado com 2 casas após o ponto.
'''

'''
Solution 1
piece_one = input().split()
piece_two = input().split()

code_one = int(piece_one[0])
quantity_one = int(piece_one[1])
price_one =  float(piece_one[2])
code_two = int(piece_two[0])
quantity_two = int(piece_two[1])
price_two =  float(piece_two[2])


total = (quantity_one * price_one) + (quantity_two * price_two)

print("VALOR A PAGAR: R$ {}".format(format(total, '.2f')))
'''

'''
Solution 2
piece_one = input().split()
piece_two = input().split()

total = (int(piece_one[1]) * float(piece_one[2])) + (int(piece_two[1]) * float(piece_two[2]))

print("VALOR A PAGAR: R$ {}".format(format(total, '.2f')))
'''

# Solution 3
code1, quantity1, price1 = [item for item in input().split()]
code2, quantity2, price2 = [item for item in input().split()]

total = (int(quantity1) * float(price1)) + (int(quantity2) * float(price2))

print("VALOR A PAGAR: R$ {}".format(format(total, '.2f')))
