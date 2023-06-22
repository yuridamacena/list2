x = float(input('Primeiro lado: '))
y = float(input('Segundo  lado: '))
z = float(input('Terceiro lado: '))

if (x + y < z) or (x + z < y) or (y + z < x):
        print('Nao é um triangulo')

elif (x == y) and (x == z) :
        print('Equilatero')

elif (x==y) or (y==z) or (y==z):
        print('Isósceles')

else:
       print('Escaleno')