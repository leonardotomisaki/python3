m = int(input('Digite uma distância em metros:'))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('A quantidade de {} metros equivale a: \n{:.0f} km, \n{:.0f} hm,\n{:.0f} dam, \n{:.0f} dm, \n{:.0f} cm, \n{:.0f} mm'.format(m, km, hm, dam, dm, cm, mm))