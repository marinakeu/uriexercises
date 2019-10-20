'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos
quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre
eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = √(x2 - x1)² + (y2 - y1)²

Entrada
O arquivo de entrada contém duas linhas de dados.
A primeira linha contém dois valores de ponto flutuante:
x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida,
com 4 casas após o ponto decimal.
'''

'''
Solution 1
import math

p1 = input().split()
x1 = float(p1[0])
y1 = float(p1[1])

p2 = input().split()
x2 = float(p2[0])
y2 = float(p2[1])

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("{}".format(format(distancia, '.4f')))
'''

# Solution 2
import math

p1 = input().split()
x1 = float(p1[0])
y1 = float(p1[1])

p2 = input().split()
x2 = float(p2[0])
y2 = float(p2[1])

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("{:.4f}".format(distancia))