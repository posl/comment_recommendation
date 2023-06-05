def getNums(N):
    nums = []
    
    for i in range(1, 10):
        num = 1
        while num <= N:
            if num == N:
                nums.append(num)
                return nums
            nums.append(num)
            num *= i
            
    return nums
