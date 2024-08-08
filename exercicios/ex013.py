salario = int(input('Digite o valor de seu salário: R$'))
aumento = (15/100*salario) + salario
print('O seu salário com 15% de aumento é R${:.0f}'.format(aumento))