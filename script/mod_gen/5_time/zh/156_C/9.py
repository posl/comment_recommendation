def min_sum(nums):
    #计算最小值
    min_num = min(nums)
    #计算最大值
    max_num = max(nums)
    #计算最小值和最大值之间的差值
    diff = max_num - min_num
    #初始化最小值
    min_sum = 100000000
    #遍历最小值和最大值之间的差值
    for i in range(diff):
        #计算体力值
        sum = 0
        #遍历所有的坐标值
        for j in nums:
            #计算体力值
            sum += (j - min_num - i) ** 2
        #如果体力值小于最小值，则赋值给最小值
        if sum < min_sum:
            min_sum = sum
    #返回最小值
    return min_sum

if __name__ == '__main__':
    min_sum()