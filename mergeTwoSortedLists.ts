const mergeTwoSortedLists = (nums1: number[], nums2: number[]): number[] => {
  nums1 = nums1.filter(n => n !== 0)

  return (nums1.concat(nums2)).sort((nums1, nums2) => nums1 - nums2)
}

console.log(mergeTwoSortedLists([4,8,12,16,0,0,0], [11,12,13]))
console.log(mergeTwoSortedLists([1,2,3,0,0,0],[2,5,6]))