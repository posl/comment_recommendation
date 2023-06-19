def findSingleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == '__main__':
    findSingleNumber()