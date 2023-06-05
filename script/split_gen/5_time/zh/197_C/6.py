def get_min_xor(nums):
    nums.sort()
    min_xor = nums[0] ^ nums[1]
    for i in range(1, len(nums) - 1):
        min_xor = min(min_xor, nums[i] ^ nums[i + 1])
    return min_xor
