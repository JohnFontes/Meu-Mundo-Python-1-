print('Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo')

a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('Sim, é possível criar um retângulo com essas medidas!')
else: 
    print('Não, não é possível criar um triângulo com essas medidas!')
