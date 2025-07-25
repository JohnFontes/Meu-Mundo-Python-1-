print('Faça um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta pinta uma área de 2m²')

altura = float(input('Digita a altura: '))
largura = float(input('Digita a largura: '))
área = altura*largura

print(f'A área é igual a: {área}m²')
print(f'Para pintar a parade será preciso de {área/2} litros de tinta')