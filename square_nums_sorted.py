def square_nums_sorted(nums):
  nums = [pow(x,2) for x in nums]
  return sorted(nums)


if __name__ == '__main__':
  square_nums_sorted([-4,-1,0,3,10])
  square_nums_sorted([-7,-3,2,3,11])
