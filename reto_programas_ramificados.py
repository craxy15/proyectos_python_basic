usuario_1 = input('Como te llamas? ')
edad_1 = int(input('Cuantos anos tienes? '))

usuario_2 = input('Como te llamas? ')
edad_2 = int(input('Cuantos anos tienes? '))

if edad_1 > edad_2 :
    print(f'{usuario_1} es mayor que {usuario_2}')
elif edad_1 < edad_2 :
    print(f'{usuario_1} es menor que {usuario_2}')
else:
    print('Los dos teneis la misma edad.')
