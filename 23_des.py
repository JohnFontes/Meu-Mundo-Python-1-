print('Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.')

num=(input('Digite um número entre 0 a 9999: ')).zfill(4) #.zfill () adiciona zeros a esquerda, ocupando 4 caracteres
num_div=(num.split())

print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')

#num = int(input("Digite um número entre 0 a 9999: "))

#unidade = num % 10
#dezena = (num // 10) % 10
#centena = (num // 100) % 10
#milhar = (num // 1000) % 10

#print(f"Unidade: {unidade}")
#print(f"Dezena: {dezena}")
#print(f"Centena: {centena}")
#print(f"Milhar: {milhar}")
