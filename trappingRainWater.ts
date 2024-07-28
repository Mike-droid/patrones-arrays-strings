const trap = (height: number[]): number => {
  if (height.length < 3) {
    return 0;
  }

  let leftPointer = 0
  let rightPointer = height.length - 1
  let maximumHeightLeft = 0
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
      waterSquares += maximumHeightLeft - height[leftPointer]
      leftPointer += 1
    } else {
      waterSquares += maximumHeightRight - height[rightPointer]
      rightPointer -= 1
    }
  }

  return waterSquares;
}

console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1])) //* = 6
console.log(trap([4,2,0,3,2,5])) //* = 9
