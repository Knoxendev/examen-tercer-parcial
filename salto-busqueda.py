import math
from numbers import Number

lista = None
tamano = None
buscado = None
prueba = None
indice = None
pruebaValor = None
cambiosSalto = None
resultado = None
salto = None

# Describe this function...
def saltoBusqueda(lista, tamano, buscado):
  global prueba, indice, pruebaValor, cambiosSalto, resultado, salto
  indice = 0
  cambiosSalto = 1
  salto = math.floor(math.sqrt(tamano))
  if lista[0] == buscado:
    return [0, 0]
  while lista[int(((min([salto, tamano]) - 1) + 1) - 1)] < buscado:
    indice = salto
    salto = (salto if isinstance(salto, Number) else 0) + math.floor(math.sqrt(tamano))
    cambiosSalto = (cambiosSalto if isinstance(cambiosSalto, Number) else 0) + 1
    if indice >= tamano:
      return [-1, cambiosSalto]
  while lista[int((indice + 1) - 1)] < buscado:
    indice = (indice if isinstance(indice, Number) else 0) + 1
    if indice == min([salto, tamano]):
      return [-1, cambiosSalto]
  if lista[int((indice + 1) - 1)] == buscado:
    return [indice, cambiosSalto]
  return [-1, cambiosSalto]

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

prueba = '0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610'.split(',')
prueba = [int(x) for x in prueba]
pruebaValor = float(text_prompt('Ingrese el valor a buscar: '))
resultado = saltoBusqueda(prueba, len(prueba), pruebaValor)
if resultado[0] >= 0:
  print(''.join([str(x) for x in ['El número ', pruebaValor, ' se encontró en la posición ', resultado[0], ' con ', resultado[1], ' saltos en la búsqueda.']]))
else:
  print(''.join([str(x2) for x2 in ['Se realizaron ', resultado[1], ' saltos para buscar el número ', pruebaValor, ' en el arreglo de longitud ', len(prueba), ', pero no se encontró.']]))