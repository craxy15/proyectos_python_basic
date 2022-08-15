#Reto utilizanto el ciclo for/while/breake/continue

def run():
    nombre = input('Escribe tu frase favorita: ')
    for i in nombre :
        print(i)
    while len(nombre)< 8:
        print('Tiene que tener al menos 8 caracteres!')
        break



if __name__ == '__main__':
    run()