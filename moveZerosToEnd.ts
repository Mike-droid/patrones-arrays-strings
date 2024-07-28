const moveZerosToEnd = (nums: number[]): number[] => {
  if (nums.length === 1) {
    return nums
  }

  let countZeros = 0

  for (let index = 0; index < nums.length; index++) {
    if (nums[index] === 0) {
      countZeros += 1
      nums.splice(index, 1)
    }
  }

  while (countZeros > 0) {
    nums.push(0)
    countZeros -= 1
  }

  return nums
}

console.log(moveZerosToEnd([0,1,0,3,12])); //* [1,3,12,0,0]
console.log(moveZerosToEnd([0]));//* [0]