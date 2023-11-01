def checkPair(nums):
    temp = set()
    for num in nums:
        if num in temp:
            return "NO"
        else:
            temp.add(num)
    return "YES"

if __name__ == '__main__':
    checkPair()