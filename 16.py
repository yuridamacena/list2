print('Digite a equalção do 2°grau (ax²+bx+c) ')
a = float(input('Coeficiente a:'))

if a ==0:
    print('Se a e igual a 0, não e uma equação de segundo grau. finalizado')

else:
    b = int(input('Coeficiente b'))
    c = int(input('Coeficiente c'))

delta = b*b - (4*a*c)

if delta < 0:
    print('delta não existe pois a raiz e negativa. finalizado')

elif delta == 0:
    raiz = -b / (2*a)
    print('Delta=0 , raiz', raiz)

else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print('Raizes:', raiz1,'e',raiz2)