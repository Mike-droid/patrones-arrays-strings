const trap = (height: number[]): number => {
  if (height.length < 3) {
    return 0;
  }

  let leftPointer = 0
  let rightPointer = height.length - 1

  const heightsLeft: number[] = []
  let maximumHeightLeft = 0

  const heightsRight: number[] = []
  let maximumHeightRight = 0

  let waterSquares = 0

  while (leftPointer < rightPointer) {
    if (maximumHeightLeft < height[leftPointer]) {
      maximumHeightLeft = height[leftPointer]
    }
    if (maximumHeightRight < height[rightPointer]) {
      maximumHeightRight = height[rightPointer]
    }

    if (height[leftPointer] < height[rightPointer]) {
      heightsLeft.push(height[leftPointer])
      waterSquares += maximumHeightLeft - height[leftPointer]
      leftPointer += 1
    } else {
      heightsRight.push(height[rightPointer])
      waterSquares += maximumHeightRight - height[rightPointer]
      rightPointer -= 1
    }
  }

  return waterSquares;
}

console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1])) //* = 6
console.log(trap([4,2,0,3,2,5])) //* = 9
