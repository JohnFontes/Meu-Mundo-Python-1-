print('Crie um programa que leia um número real qualquer pelo teclado e mostre na tela e sua porção inteira')

import math 

num = float(input('Digite um número racional: '))
Q = math.trunc(num)

print(f'O número {num} tem a parte inteira {Q}')