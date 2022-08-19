import math

izq = None
der = None
buscado = None
lista = None
prueba = None
resultado = None
mid1 = None
pruebaValor = None
mid2 = None

# Describe this function...
def busquedaTernaria(izq, der, buscado, lista):
  global prueba, resultado, mid1, pruebaValor, mid2
  if der >= izq:
    mid1 = izq + math.floor((der - izq) / 3)
    mid2 = der - math.floor((der - izq) / 3)
    if lista[int((mid1 + 1) - 1)] == buscado:
      return mid1
    if lista[int((mid2 + 1) - 1)] == buscado:
      return mid2
    if buscado < lista[int((mid1 + 1) - 1)]:
      resultado = busquedaTernaria(izq, mid1 - 1, buscado, lista)
    elif buscado > lista[int((mid2 + 1) - 1)]:
      resultado = busquedaTernaria(mid2 + 1, der, buscado, lista)
    else:
      resultado = busquedaTernaria(mid1 + 1, mid2 - 1, buscado, lista)
  else:
    resultado = -1
  return resultado

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


prueba = '1,2,3,4,5,6,7,8,9,10'.split(',')
prueba = prueba = [int(x) for x in prueba]
for count in range(2):
  pruebaValor = float(text_prompt('Ingrese el número a buscar: '))
  resultado = busquedaTernaria(0, len(prueba) - 1, pruebaValor, prueba)
  if resultado >= 0:
    print(''.join([str(x) for x in ['El número ', pruebaValor, ' se encontró en la posición ', resultado]]))
  else:
    print('Número no encontrado.')
