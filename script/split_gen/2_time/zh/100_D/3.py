def get_max(n,m,nums):
    max = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i!=j and j!=k and i!=k:
                    tmp = abs(nums[i][0])+abs(nums[j][1])+abs(nums[k][2])
                    if tmp>max:
                        max = tmp
    return max
