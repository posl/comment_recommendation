def find_min_index(nums):
    min_index = 0
    min_num = nums[0]
    for i in range(1,len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]
            min_index = i
    return min_index

if __name__ == '__main__':
    find_min_index()