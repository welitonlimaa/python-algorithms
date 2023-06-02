def find_duplicate(nums):
    for target in nums:
        i = nums.index(target)
        del nums[i]
        if target in nums and target >= 0:
            return target
    return False


print(find_duplicate([1, 3, 4, 2, 2]))
