print('Crie um programa que leia o nome completo de uma pessoa e mostre')

nome = str(input('Digite um nome completo: '))
nome_sem_espaço = nome.replace(' ', '')
nome_divido = (nome.split())

print(f'Nome com todas as letras maisculas: {nome.upper()}') #nome com todas letras maisculas
print(f'Nome com todas as letras minusculas: {nome.lower()}') #nome com todas as letras minusculas
#print(f'Quantidade de caracteres sem contar os espaços: {len(nome_sem_espaço)}') #Quantas letras tem, sem considerar os espaços 
print(f'Quantidade de caracteres sem contar os espaços: {len(nome)-(nome.count(' '))}') #Quantas letras tem, sem considerar os espaços 
#print(f'Quantidade de letras presente no primeiro nome: {nome.find(' ')}') #Quantas letras tem o primeiro nome
print(f'Seu primeiro nome é: {nome_divido[0]} e ele tem {len(nome_divido[0])} letras') #Mostra o primeiro nome e quantas letras tem
