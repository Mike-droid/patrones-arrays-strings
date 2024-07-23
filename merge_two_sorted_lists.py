def merge_two_sorted_lists(nums1, nums2):
    nums1 = [n for n in nums1 if n != 0]
    return sorted(nums1 + nums2)

# Test the function
print(merge_two_sorted_lists([4, 8, 12, 16, 0, 0, 0], [11, 12, 13]))
print(merge_two_sorted_lists([1, 2, 3, 0, 0, 0], [2, 5, 6]))
