din = float(input('Digite quanto dinheiro você tem na carteira: R$'))
dolar = din/5.57
euro = din/6.08
print('Com R${:.0f} reais você pode comprar US${}'.format(din, dolar))
print('Com R${:.0f} você pode comprar €{}'.format(din, euro))