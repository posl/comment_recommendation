def cutbar(m, n, current):
    if current >= n:    #如果当前长度大于等于目标长度，返回0
        return 0
    elif current < m:   #如果当前长度小于初始长度，返回1+递归
        return 1 + cutbar(m, n, current * 2)
    else:               #如果当前长度大于等于初始长度，返回1+递归
        return 1 + cutbar(m, n, current + m)
print(cutbar(3, 20, 1))
