a = float(input('Digite o primeiro valor:'))
b = float(input('Digite o segundo valor:'))
c = float(input('Digite o terceiro valor:'))

if a < 2 or a < b:
    print(f'O produto com menor preço é o primeiro, com valor de R$ {a :.2f}')

elif b < a or b < c:
    print(f'O produto com menor preço é o segundo, com valor de R${b :.2f}')
    
else:
    print(f'O produto com menir valor é o terceiro, com valor de R$ {c :.2f}')