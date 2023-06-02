# def binary_search(numbers, target):
#     start = 0
#     end = len(numbers) - 1

#     while start <= end:
#         mid = (start + end) // 2

#         if numbers[mid] == target:
#             return mid
#         if target < numbers[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return False


def find_duplicate(nums):
    for target in nums:
        i = nums.index(target)
        del nums[i]
        if target in nums and target >= 0:
            return target
    return False


print(find_duplicate([1, 3, 4, 2, 2]))
