brl = input('Qual valor você deseja trocar?: ')
brl = float(brl)
usd = 5.48
cambio = brl/usd
print(f'Você quer trocar R${brl:.2f} para dolar, a uma taxa de ${usd:.2f}')
print(f'Você receberá ${cambio:.2f}')