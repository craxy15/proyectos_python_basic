from math import factorial


def es_primo(numero):
    contador = 0
    if (factorial(numero-1) + 1) %numero == 0:
        return True
    else:
        return False


def run():
    numero =int(input('Escribe un numero: '))
    if es_primo(numero):
        print('Es numero primo')
    else:
        print('No es numero primo')


if __name__ == '__main__':
    run()