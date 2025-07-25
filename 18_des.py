print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cposseno e tangente')

import math

angulo_graus = int(input('Digite o valor do ângulo: '))
angulo_rad = math.radians(angulo_graus)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")
