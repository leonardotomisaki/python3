n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1+n2)/2
print('Sua média é {}'.format(m))
if m <5:
    print('Você está reprovado!')
else:
    print('Você está aprovado!')
