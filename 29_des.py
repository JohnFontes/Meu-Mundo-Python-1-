print('''Escreve um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi mutado.
A multa vai custar R$7,00 por cada Km acima do limite.\n''')

velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 85:
    excesso = velocidade - 85
    multa = excesso * 7
    print(f'Você ultrapassou {excesso}Km/h')
    print(f'Você terá que pagar uma multa de R${multa}') 
else:
    print('Você está dentro do limite de velocidade. Dirija com segurança!')

