def func(n,k,nums):
    nums.sort()
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            count += 1
            if count == k:
                return nums[i]*nums[j]
    return 0

if __name__ == '__main__':
    func()