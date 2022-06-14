euro = input('Cuantos euros tienes?: ')
euro = float(euro)
valor_dolar = 1.06
dolares = euro * valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print('Tienes $' + dolares + ' dolares')