def permute(nums):
    res = []
    def backtrack(nums, tmp):
        if not nums:
            res.append(tmp)
            return
        for i in range(len(nums)):
            backtrack(nums[:i]+nums[i+1:], tmp+[nums[i]])
    backtrack(nums, [])
    return res
