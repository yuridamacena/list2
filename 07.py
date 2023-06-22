n1 = float(input('Digite o primeiro numero:'))
n2 = float(input('Digite o segundo numero:'))
n3 = float(input('Digite o terceiro numero:'))

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
    
if n3 > n1 and n3 > n2:
    maior = n3
    
menor = n1

if n2 < n3 and n2 < n1:
    menor = n2

if n3 < n2 and n3 < n1:
    menor = n3
    
print('O maior numero digitado foi:', maior)
print('O menor numero digitado foi:', menor)