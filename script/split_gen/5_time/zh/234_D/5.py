def get_max_k_num(nums, k):
    # 从大到小排序
    nums.sort(reverse=True)
    return nums[k-1]
