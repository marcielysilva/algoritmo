n = int(input('digite em dias: '))

ano = n // 365
n = n - ano * 365

mes = n // 30
n = n - mes * 30

d = n

print('{} anos'.format(ano))
print('{} mes'.format(mes))
print('{} dias'.format(d))





