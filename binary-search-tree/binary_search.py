def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while (l <= r):
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1


def binary_search_floor(nums, target):
    l, r = 0, len(nums) - 1
    while (l <= r):
        mid = (l + r) // 2
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] != target:
                return mid
            else:
                r = mid - 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return l - 1


def binary_search_ceil(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                return mid
            else:
                l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return r + 1