"""
Find Pivot Index leet code 724

ex) 
nums = [1, 8, 2, 9, 2, 3, 6]
nums = [2, 5, 7]

pivot이란 pivot을 중심으로 pivot 왼쪽의 합과
오른쪽의 합이 같은 pivot의 index return

first approach is Brute Force
O(n) * n = O(n^2)으로 이 보다는 효율적인 풀이어야 한다.

먼저 전체 sum을 계산 후 pivot 1을 빼준다.
왼쪽  | 오른쪽
0     | sum(nums) - 1
1     | sum(nums) - 1 - 8
1 + 8 | sum(nums) - 1 - 8 -2

time complexity는 O(1)이동 * n 번 + O(n) sum = O(n)
"""
def pivotIndex(nums: list) -> int:
    left = 0
    right = sum(nums)
    prvnum = 0
    for i in range(len(nums)):
        num = nums[i]
        right = right - num
        left = left + prvnum
        if left == right:
            return i
        prvnum = num

# nums = [1, 8, 2, 9, 2, 3, 6]

# print(pivotIndex(nums))

"""
leet code 209 Minimum Size Subarray Sum

target num = 7
nums = [3, 4, 2, 1, 3, 2]에서 target을 만족하는 
짧은 subarray를 길이를 return을 하는것 -> O(n)

전제조건은 nums array가 positive integer인 경우에만 
sliding을 사용 할 수 있다.
"""
def minSubArrayLen(target: int, nums: list) -> int:
    left = 0
    right = len(nums) - 1

    for i in range(len(nums)):
        add = sum(nums[:i])
        print(add)     
print('---',minSubArrayLen(target = 7, nums = [3, 4, 2, 1, 3, 2]))