def get_min_xor_sum(nums):
    min_xor_sum = nums[0]
    for i in range(1, len(nums)):
        min_xor_sum ^= nums[i]
    return min_xor_sum
