tipoCombustivel = input('Digite(A) para Alcool ou (G) para Gasolina: ').upper()
quantidadeLitros = float(input('Digite a quantidade de litros: '))

if (tipoCombustivel == 'A'):
    valor = 1.9
    if (quantidadeLitros <= 20):
        desconto = 3
    else:
        desconto = 5

else:
    valor = 2.5
    if (quantidadeLitros <= 20):
        desconto = 4
    else:
        desconto = 6

totalPagar = (valor * quantidadeLitros) * ((100 - desconto) / 100.0)
print ('Total a pagar: ', totalPagar)