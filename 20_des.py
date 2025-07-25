print('O mesmo professor do desafio anterior que sortear a ordem de apresentação de trabalho dos alunos, faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada')

import random

#aluno1 = input("Digite o nome do 1º aluno: ")
#aluno2 = input("Digite o nome do 2º aluno: ")
#aluno3 = input("Digite o nome do 3º aluno: ")
#aluno4 = input("Digite o nome do 4º aluno: ")

# Colocando os nomes dentro de uma lista
#alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralhando a lista
#random.shuffle(alunos)

#print('A ordem de apresentação será:')
#print(alunos[0])
##print(alunos[1])
#print(alunos[2])
#rint(alunos[3])

n1 = input('Primeiro aluno: ')
n2 = input('Sefundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)