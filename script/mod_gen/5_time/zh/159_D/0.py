def cal(nums):
    n = len(nums)
    if n < 2:
        return 0
    nums.sort()
    i = 0
    j = 1
    count = 0
    while i < n and j < n:
        if nums[i] == nums[j]:
            count += 1
            j += 1
        elif nums[i] < nums[j]:
            i += 1
            j += 1
        else:
            i += 1
    return count

if __name__ == '__main__':
    cal()