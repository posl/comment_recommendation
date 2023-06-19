def get_min_xor(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[0] ^ nums[1]
    min_xor = 0
    for i in range(1, len(nums)):
        xor = get_min_xor(nums[:i]) ^ get_min_xor(nums[i:])
        if i == 1:
            min_xor = xor
        if xor < min_xor:
            min_xor = xor
    return min_xor
