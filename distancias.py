dist = input('Digite uma distância em metros: ')

dist = float(dist)

cm1 = dist * 100
km1 = dist / 1000
mm1 = dist * 1000

print(f'A distância em cm é: {cm1:.2f}')
print(f'A distância em km é: {km1:.2f}')
print(f'A distância em mm é: {mm1:.2f}')