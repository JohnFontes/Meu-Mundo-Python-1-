print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa')

from math import pow,sqrt,hypot

cad = int(input('Digite o valor do cateto adjacente: '))
cop = int(input('Digite o valor do cateto oposto: '))
#hip = int(sqrt((pow(cad,2)+pow(cop,2))))
hip = int(hypot(cad,cop))

print(f'O valor da hipotenusa é igual a: {hip}')