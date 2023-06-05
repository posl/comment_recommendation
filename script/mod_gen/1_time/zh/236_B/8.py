def findMissingNumber(n, nums):
    numDict = {}
    for i in range(len(nums)):
        if nums[i] not in numDict:
            numDict[nums[i]] = 1
        else:
            numDict[nums[i]] += 1
    for i in range(1, n+1):
        if i not in numDict:
            return i
        elif numDict[i] < 4:
            return i
    return 0
n = int(input())
nums = list(map(int, input().split()))
print(findMissingNumber(n, nums))
