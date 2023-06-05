def get_max_min_diff(nums):
    max_num = max(nums)
    min_num = min(nums)
    max_diff = max_num - min_num
    return max_diff

if __name__ == '__main__':
    get_max_min_diff()