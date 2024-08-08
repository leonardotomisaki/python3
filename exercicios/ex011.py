larg = float(input('Digite uma largura de parede:'))
alt = float(input('Digite uma altura de parede:'))
area = larg * alt
tinta = area/2
print('Uma parede de {} m de largura e {} m de altura, tem uma área a de {}m² e é necessário {} litros de tinta para pintar'.format(larg, alt, area, tinta))