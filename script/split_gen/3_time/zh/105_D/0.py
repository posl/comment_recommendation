def num_of_divisible_subarray(nums, m):
    n = len(nums)
    num_of_divisible_subarray = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum % m == 0:
                num_of_divisible_subarray += 1
    return num_of_divisible_subarray
