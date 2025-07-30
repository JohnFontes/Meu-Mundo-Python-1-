print('''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$O,50 por km para viagens de até 200Km e R$0,45 para viagens mais longas.\n''')

km_viagem = int(input('Digite a distância a ser percorrida na viagem: '))

if km_viagem <= 200:
    preço = km_viagem*0.50
    print(f'O preço da passagem é: R${preço}.')
else:
    preço_2 = km_viagem*0.45
    print(f'O preço da passagem é: R${preço_2}')


