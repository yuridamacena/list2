num1 = float(input('Digite a primeira nota:'))
num2 = float(input('Digite a segunda nota:'))
num3 = float(input('Digite a terceira nota:'))

maior = num1

if (num2 > maior):
    maior = num2

if (num3 > maior):
    maior = num3

print('O maior nota é:', maior)