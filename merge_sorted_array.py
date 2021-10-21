"""
두 개의 정렬된 리스트를 하나로
leetcode 88 merge sorted array

[1, 3, 5, 0, 0, 0]   m = 3
[2, 4, 8] n = 3
    ↓
[1, 2, 3, 4, 5, 8]
즉 새로운 리스트를 만드는 것이 아닌 첫 리스트에 merge

즉 두 리스트를 큰 숫자들 부터 비교해서

첫 번째 리스트의 0 부분부터 채워나가면 된다.

time complexity = O(n + m)
space complexity = O(1)
"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    num1idx = m - 1 # 첫 번째 리스트의 0이 아닌 숫자의 가장 큰 수의 pointer
    num2idx = n - 1 # 두 번째 리스트의 가장 큰 수의 pointer
    widx = len(nums1) - 1

    if num2idx < 0:
        return 

    while 0 <= num1idx and 0 <= num2idx:
        num1 = nums1[num1idx]
        num2 = nums2[num2idx]
        if num2 <= num1:
            num = num1
            nums1[widx] = num
            num1idx -= 1
            widx -= 1
        else:
            num = num2
            nums1[widx] = num
            num2idx -= 1
            widx -= 1

    # while 0 <= num2idx:
    #     nums1[widx] = nums2[num2idx]
    #     nums2idx -= 1
    #     widx -= 1
    print(nums1)


nums1 = [1, 3, 5, 0, 0, 0] 
m = 3
nums2 = [2, 4, 8]
n = 3

merge(nums1, m, nums2, n)