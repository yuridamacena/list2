inicio = int(input('Digite o ano: '))
fim = int(input('Digite o ano final: '))
calculo = (inicio % 4 == 0 and inicio % 100 != 0) or (inicio % 400 == 0)
contagem = 0

for x in range(inicio, fim+1):
    if calculo:
        pass
    else:
        contagem +=1
        print(f'{x}')
print(f'bissextos: {contagem}')