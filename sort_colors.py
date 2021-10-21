"""
leetcode 75 sort colors

nums = [1, 0 , 2, 2, 0, 1, 2, 1, 0]

[0, 0, 0, 1, 1, 1, 2, 2, 2]
-> O(nlogn)
-> O(n) hash map
-> in-place swap

quick sort - pivot
           - partition
this problem is related with quick sort (two pointer)
"""
def sortColors(nums: list) -> None:
    start, mid, end = 0, 0, len(nums) - 1

    while mid < end:
        if nums[mid] < 1:
            nums[start], nums[mid] = nums[mid], nums[start]
            mid += 1
            start += 1
        elif nums[mid] > 1:
            end -= 1
            nums[mid], nums[end] = nums[end], nums[mid]
        else:
            mid += 1
    print(nums)

sortColors(nums = [1, 0 , 2, 2, 0, 1, 2, 1, 0])

 