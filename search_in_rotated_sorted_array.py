from typing import List


def search_in_rotated_array(nums: List[int], target: int) -> int:
  if len(nums) == 1:
    return 0 if nums[0] == target else -1

  left = 0
  right = len(nums) - 1

  while(left <= right):
    middle = (left + right) // 2
    if nums[middle] == target:
      return middle

    if nums[left] <= nums[middle]: #* left half is sorted
      if nums[left] <= target < nums[middle]:
        right = middle - 1
      else:
        left = middle + 1
    else: #* right half is sorted
      if nums[middle] < target <= nums[right]:
        left = middle + 1
      else:
        right = middle - 1

  return -1


print(search_in_rotated_array([4,5,6,7,0,1,2], 0)) # 4 - length 7
print(search_in_rotated_array([4,5,6,7,8,9,10,11,0,1,2], 0)) # 8 - length 11
print(search_in_rotated_array([4,5,6,7,8,9,10,11,1,2], 7)) # 3 - length 10
print(search_in_rotated_array([7,8,9,10,11,0,1,2,6], 8)) # 1 - length 9
print(search_in_rotated_array([4,5,6,7,0,1,2], 3)) # -1
print(search_in_rotated_array([1], 0)) # -1
