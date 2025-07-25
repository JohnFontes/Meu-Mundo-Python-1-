#teste = input('Digite um número: ') #Independene do valor que eu coloque, sempre retornará uma string, pelo fato de estar das aspas
#print(teste.isalpha())


print ('==== Desafio 4 =====')

valor = input("Digite algo: ")

print("Informações sobre o valor digititado: ")
print(f"Tipo primitivo: {type(valor)}")
print(f'Só tem espaços? {valor.isspace()}')
print(f'É númerico? {valor.isnumeric()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'É alfanumérico? {valor.isalnum()}')
print(f'Está em maiúsculas? {valor.isupper()}')
print(f'Está em minúsculas? {valor.islower()}')
print(f'Está capitalizada ? {valor.istitle()}')