print('Faça um program que leia 3 números e mostre qual é o maior e qual o menor entre eles')

n1 = int(input('Insira um valor: '))
n2 = int(input('Insira um valor: '))
n3 = int(input('Insira um valor: '))
maior = max(n1,n2,n3)
menor = min(n1,n2,n3)

print(f'\nO maior número é: {maior}')
print(f'O menor número é: {menor}')