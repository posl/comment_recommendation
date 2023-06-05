def getNum():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums)
    if nums[0] != nums[1]:
        print(nums[0])
    elif nums[-1] != nums[-2]:
        print(nums[-1])
    else:
        for i in range(1, len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                print(nums[i])
                break
getNum()
