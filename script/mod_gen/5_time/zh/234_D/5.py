def get_max_k_num(nums, k):
    # 从大到小排序
    nums.sort(reverse=True)
    return nums[k-1]

if __name__ == '__main__':
    get_max_k_num()