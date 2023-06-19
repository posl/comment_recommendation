def find_seq(nums, mod):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] + nums[j]) % mod == 0:
                return (i,j)
    return None
