def checkNums(nums):
    if len(nums) != len(set(nums)):
        return False
    else:
        return True
