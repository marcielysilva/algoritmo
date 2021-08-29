
c = 1
for i in range(1, 2, +1):
    a = int(input('digite um valor: '))
    b = int(input('digite um segundo valor: '))
    if a <= b:
        print(a)
    elif c >=a and c <= b:
        print(c)
        a = a + 1
    else:
        print(b)
    print(a,a+1, b, end=' ')