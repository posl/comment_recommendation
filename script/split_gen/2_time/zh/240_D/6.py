def solve(n, a):
    # write code here
    nums = []
    for i in range(n):
        nums.append(a[i])
        while len(nums) >= 2 and nums[-1] == nums[-2]:
            nums.pop()
            nums.pop()
    return nums
