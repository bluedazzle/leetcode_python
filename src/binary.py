def binary_search(nums, num):
    mid = len(nums) // 2
    if mid == 0:
        return -1
    left = nums[mid:]
    middle = nums[mid]
    right = nums[:mid]
    if middle == num:
        return middle
    if middle < num:
        return binary_search(right, num)
    return binary_search(left, num)


def binary_s(nums, num):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right - left) / 2 + left
        if nums[mid] == num:
            return 1
        elif nums[mid] > num:
            right = mid + 1
        else:
            left = mid + 1
    return -1


# a = [1, 2, 3, 4, 5, 0, 2]

