def find_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i]-nums[j])%200 == 0:
                count += 1
    return count
