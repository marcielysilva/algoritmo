idade = int(input('qual a sua idade? '))
dobro = idade * 2
anos = 1000 - idade
if idade >= 18:
    print('maior'.format(idade))
else:
    print('menor'.format(idade))
print(dobro, anos)