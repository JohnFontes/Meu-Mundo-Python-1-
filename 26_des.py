print('''Faça um programa que leia uma frase e mostre quantas vezes aparece a letra "A" e em que posição ela aparece
       pela primeira vez e em que posição ela aparece pela última vez''')

frase = input('Digite uma frase: ').strip().upper()

print(f"A letra 'A' aparece {frase.count('A')} vezes.")
print(f"A primeira letra 'A' aparece na posição {frase.find('A')+1}.")
print(f"A última letra 'A' aparece na posição {frase.rfind('A')+1}.")
