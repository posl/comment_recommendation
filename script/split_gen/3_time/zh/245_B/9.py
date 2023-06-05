def getMinNotInList(nums):
    nums.sort()
    min = 0
    for num in nums:
        if num > min:
            return min
        elif num == min:
            min += 1
    return min
