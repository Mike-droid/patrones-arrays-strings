const containerWithMostWater = (alturas: number[]): number => {
  const alturasCopy = [...alturas]

  const biggestNumber = alturasCopy.sort((a,b) => b-a)[0]

  const secondBiggestNumberArray = alturasCopy.sort((a,b) => b-a)

  let secondBiggestNumber = Number.NEGATIVE_INFINITY
  for (let index = 0; index < secondBiggestNumberArray.length; index++) {
    if (secondBiggestNumberArray[index] < biggestNumber) {
      secondBiggestNumber = secondBiggestNumberArray[index]
      break
    }
  }

  const indexesOfBiggestNumbers: number[] = []
  for (let index = 0; index < alturas.length; index++) {
    if (alturas[index] === biggestNumber) {
      indexesOfBiggestNumbers.push(index)
    }
  }

  const indexesOfSecondBiggestNumbers: number[] = []
  for (let index = 0; index < alturas.length; index++) {
    if (alturas[index] === secondBiggestNumber) {
      indexesOfSecondBiggestNumbers.push(index)
    }
  }

  let distance: number = Number.NEGATIVE_INFINITY
  const secondBiggestNumberBiggestIndex = indexesOfSecondBiggestNumbers.pop()

  distance = secondBiggestNumberBiggestIndex! - indexesOfBiggestNumbers[0]

  return distance * secondBiggestNumber
}

console.log(containerWithMostWater([1,8,6,2,5,4,8,3,7]))
console.log(containerWithMostWater([9,8,8,7,5,4,8,9,3,7,8,8,7,1,1,1,1,1,1,5,4,9]))

/*
1. encontrar el número más grande
2. encontrar el segundo número más grande
3. encontrar la distancia más larga entre estos dos números
3.1 ¿guardar los índices de todos los números iguales al más grande?
3.2 ¿guardar los índices de todos los números iguales al segundo más grande?
3.3 calcular la distancia de los más alejados
4. multiplicar el segundo número más grande por la distancia más larga
*/