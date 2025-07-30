print('''Escreve um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
\npara salários superiores a R$1.250,00, calcule um aumento de 10%.
\npara os inferiores ou iguais, o aumento é de 15%.''')

salário = float(input('\nDigite o salário: '))

if salário >= 1250.00:
    print(f'\nVocê receberá um aumento de 10% e eu novo salário será R${salário*0.10+salário}')
else:
    print(f'\nVocê receberá um aumento de 15% e eu novo salário será R${salário*0.15+salário}')
