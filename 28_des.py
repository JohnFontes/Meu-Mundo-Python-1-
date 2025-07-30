print('Escreva um programa que faça um computador pensar em um número entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador')

import random

n = int((random.randint(1,5)))
nn = int(input('Digite um número: '))

if nn==n:
    print('Parabéns você acertou o número que eu estava pensando!!')
else: 
    print(f'Poxa, não foi dessa... Eu estava pensando no {n}, tente novamente!!')