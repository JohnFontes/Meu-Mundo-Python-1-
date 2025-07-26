print('Faç um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.')

nome = input('Digite o nome completo da pessoa: ')

print('----'*20)

print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[-1]}') #usando -1 para pegar o último elemento da lista

print('----'*20)