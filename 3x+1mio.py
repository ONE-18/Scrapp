a = int(input('inicio: '))
mayor = 0
cont = 0
print('\n' + str(a))

while a != 1:
    if (a % 2) == 0:
        a = a / 2
        print(a)
    else:
        a = a * 3 + 1
        print(a)

    if a > mayor:
        mayor = a
    cont += 1
print('\nNúmero mayor:', mayor)
print('Número de pasos:', cont)

input()
