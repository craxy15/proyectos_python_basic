#Definiendo el menu
def opciones():
    menu = """
    Calcular raiz cuadrada

    Selecciona un metodo de calculo:
    1 - Enumeracion exaustiva
    2 - Aproximacion de soluciones
    3 - Busqueda binaria
    """
    print(menu)

    opcion = int(input('Selecciona un metodo: '))
    numero = int(input('Que numero quieres calcular?: '))

#Seleccionando los metodos de calculo

    if opcion == 1:
        enumeracion_exaustiva(numero)
    elif opcion == 2:
        aproximacion_de_soluciones(numero)
    elif opcion == 3 :
        busqueda_binaria(numero)
    else:
        print('Selecciona un metodo (1,2,3)')

#Primer metodo

def enumeracion_exaustiva(valor):
    respuesta = 0

    while respuesta**2 < valor:
        respuesta +=1
    
    if respuesta**2 == valor:
        print(f'La raiz cuadrada de {valor} es {respuesta}')
    else:
        print(f'{valor} no tiene una raiz cuadrada exacta')

#Segundo metodo 

def aproximacion_de_soluciones(valor):
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - valor) >= epsilon and respuesta <= valor:
        respuesta += paso

    if abs(respuesta**2 - valor) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {valor}')
    else:
        print(f'La raiz cuadrada de {valor} es {respuesta}')

#Tercer metodo

def busqueda_binaria(valor):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, valor)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - valor) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')

        if respuesta**2 < valor:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada de {valor} es {respuesta}')



opciones()
