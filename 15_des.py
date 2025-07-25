print ('Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado')

km = float(input('Quantos Km foram percorridos? '))
dias = int(input('Por quantos o carro foi alugado? '))
preço = float((60.00*dias)+(km*0.15))

print(f'O valor a pagar pelo aluguel é de R${preço:3}')