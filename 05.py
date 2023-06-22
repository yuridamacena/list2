n1 = int(input('Digite a priemeira nota:'))
n2 = int(input('Digite a segunda nota'))

nota = (n1 + n2) / 2

if nota >= 7 and nota <10:
    print('Aprovado!')
    
elif nota >= 10:
    print('Aprovado com distenção!')
    
else:
    print('Reprovado')