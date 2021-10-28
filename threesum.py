from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: 
                continue
            target = nums[i]
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                sum = nums[left] + nums[right]
                if sum + target < 0:
                    left += 1
                elif sum + target > 0:
                    right -= 1
                else:
                    result.append([target, nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    while left<right and nums[left]==nums[left-1]: 
                        left+=1
        return result

def threeSum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    
    res = []
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]: continue # ensure fixed number unique
        left,right = i+1, len(nums)-1
        while left<right:
            if nums[i]+nums[left]+nums[right]<0:
                left+=1
            elif nums[i]+nums[left]+nums[right]>0:
                right-=1
            else:
                res.append([nums[i],nums[left],nums[right]])
                left,right = left+1, right-1                
                while left<right and nums[left]==nums[left-1]: left+=1  # ensure left is unique
    return res


print(threeSum(nums = [-1,0,1,2,-1,-4]))