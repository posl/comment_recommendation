def solve(n,k,nums):
    # k-1个最大数
    res = []
    for i in range(k-1,n):
        res.append(max(nums[i-k+1:i+1]))
    return res
