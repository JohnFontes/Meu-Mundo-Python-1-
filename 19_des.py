print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escolhendo o nome escolhido')

import random

aluno1 = str(input("Digite o nome do 1º aluno: "))
aluno2 = str(input("Digite o nome do 2º aluno: "))
aluno3 = str(input("Digite o nome do 3º aluno: "))
aluno4 = str(input("Digite o nome do 4º aluno: "))

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice(alunos)

print(f'O sorteado foi o: {sorteado} ')