function isAlienSorted(palabras, orden) {
  // Crear mapa del diccionario alienigena
  const mapa_diccionario = new Map()
  for (let i = 0; i < orden.length; i++) {
    mapa_diccionario[orden[i]] = i
  }

  // Revisar el orden de las palabras
  for (let i = 1; i < palabras.length; i++) { // O(n)
    if (!comparar(palabras[i-1], palabras[i])) {
      return false
    }
  }
  return true
}

// O(longitud de la palabra más larga)
function comparar(palabra1, palabra2) {
  const longitudCorta = Math.min(palabra1.length, palabra2.length)
  for (let i = 0; i < longitudCorta; i++) {
    if (mapa_diccionario[palabra1[i]] < mapa_diccionario[palabra2[i]]) {
      return true
    }
    if (mapa_diccionario[palabra1[i]] > mapa_diccionario[palabra2[i]]) {
      return false
    }
  }
  return palabra1.length <= palabra2.length
}