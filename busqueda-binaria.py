import math

inicio = None
fin = None
lista = None
buscado = None
prueba = None
resultado = None
pruebaValor = None
centroDecimal = None
centro = None
valorCentral = None

# Describe this function...
def busquedaBinaria(inicio, fin, lista, buscado):
  global prueba, resultado, pruebaValor, centroDecimal, centro, valorCentral
  if fin >= inicio:
    centroDecimal = inicio + (fin - inicio) / 2
    centro = math.floor(centroDecimal)
    valorCentral = lista[int((centro + 1) - 1)]
    if valorCentral == buscado:
      resultado = centro
    elif valorCentral > buscado:
      resultado = busquedaBinaria(inicio, centro - 1, lista, buscado)
    else:
      resultado = busquedaBinaria(centro + 1, fin, lista, buscado)
  else:
    resultado = -1
  return resultado

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


prueba = '1,3,5,7,9,11,13,15,17,19,21,23'.split(',')
prueba = prueba = [int(x) for x in prueba]
pruebaValor = float(text_prompt('Ingrese el número a buscar: '))
resultado = busquedaBinaria(0, len(prueba) - 1, prueba, pruebaValor)
if resultado >= 0:
  print(''.join([str(x) for x in ['El valor buscado ', pruebaValor, ' se encuentra en la posición del índice ', resultado]]))
else:
  print(''.join([str(x2) for x2 in ['El valor buscado ', pruebaValor, ' no fue localizado en un arreglo de ', len(prueba), ' posiciones.']]))