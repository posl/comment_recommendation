def find_closest_num(target, nums):
    nums.sort()
    min_diff = float('inf')
    closest_num = None
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        if abs(nums[i] - target) < min_diff:
            min_diff = abs(nums[i] - target)
            closest_num = nums[i]
    return closest_num
