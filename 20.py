n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))
media = (n1 + n2 + n3) / 3.0

print ('Media do aluno: {}'.format(media))

if (media == 10):
    print ('Aprovado com Distincao')

elif (media >= 7):
    print ('Aprovado')

else:
    print ('Reprovado')