nome = str(input('Digite seu nome completo:')).strip()
print('Seu nome com apenas letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome com apenas letras minusculas é: {}'.format(nome.lower()))
print('Seu nome possui {} letras no total'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))
div = nome.split()
#print('Seu primeiro nome é {} possui {} letras'.format(div[0], len(div[0])))