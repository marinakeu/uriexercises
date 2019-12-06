'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma
mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.
'''

'''
Primeira resolução
a, b =  [int(item) for item in input().split()]

if a % b == 0 or b % a == 0:
  print("Sao Multiplos")
else:
  print("Nao sao Multiplos")
  '''

#segunda resolução
numbers =  input().split()
a = int(numbers[0])
b = int(numbers[1])

if a % b == 0 or b % a == 0:
  print("Sao Multiplos")
else:
  print("Nao sao Multiplos")