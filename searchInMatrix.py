from typing import List

def searchMatrix(matriz: List[List[int]], objetivo: int) -> bool:
  izquierda = 0
  derecha = len(matriz) - 1

  #! hard way
  while izquierda < derecha:
    mitad = izquierda + (derecha - izquierda) // 2 + 1
    if matriz[mitad][0] == objetivo:
      return True
    if matriz[mitad][0] < objetivo:
      izquierda = mitad
    else:
      derecha = mitad - 1

    fila = matriz[izquierda]
    izquierda = 0
    derecha = len(fila) - 1
    while izquierda <= derecha:
      mitad = izquierda + (derecha - izquierda) // 2
      if fila[mitad] == objetivo:
        return True
      if fila[mitad] < objetivo:
        izquierda = mitad + 1
      else:
        derecha = mitad - 1

  return False
