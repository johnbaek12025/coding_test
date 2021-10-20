def minSubArrayLen(nums, target):
    curSum = 0
    prev = 0
    ans = float("inf")
    for i in range(len(nums)):
        curSum += nums[i]
        # the while loop below is equivalent to while prev <= i and curSum >= target:
        while curSum >= target:
            ans = min(ans, i - prev + 1)
            # below order is important: the decrement of curSum and increment of prev
            curSum -= nums[prev]
            prev += 1
    if ans == float("inf"):
        return 0
    else:
        return ans  

print(minSubArrayLen(target = 4, nums = [1,4,4]))