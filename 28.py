print ('1 - File Duplo')
print ('2 - Alcatra')
print ('3 - Picanha')
tipoCarne = input('Digite o tipo da carne escolhida: ').upper()
quantidade = float(input('Digite a quantidade comprada: '))

cartao = input('Usara cartao Tabajara (S/N): ').upper()
print ('CUPOM FISCAL')

if (tipoCarne == '1'):
    print ('Carne Escolhida: File Duplo')
    if (quantidade <= 5):
        valorBruto = quantidade * 4.9
    else:
        valorBruto = quantidade * 5.8

elif (tipoCarne == '2'):
    print ('Carne Escolhida: Alcatra')
    if (quantidade <= 5):
        valorBruto = quantidade * 5.9
    else:
        valorBruto = quantidade * 6.8

else:
    print ('Carne Escolhida: Picanha')
    if (quantidade <= 5):
        valorBruto = quantidade * 6.9
    else:
        valorBruto = quantidade * 7.8
print ('Valor Bruto'), valorBruto

desconto = 0.0
if (cartao == 'S'):
    print ('Pagamento com cartao Tabajara')
    desconto = valorBruto * 0.05
else:
    print ('Pagamento nao sera com o cartao Tabajara')
print ('Desconto: '), desconto
print ('Valor a Pagar: '), (valorBruto - desconto)