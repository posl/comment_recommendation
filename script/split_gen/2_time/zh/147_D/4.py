def getPersonNum(n, a, x, y):
    max = 0
    for i in range(2**n):
        flag = True
        for j in range(n):
            if i & (1 << j):
                if not check(j, a, x, y, i):
                    flag = False
                    break
        if flag:
            max = max if max > bin(i).count('1') else bin(i).count('1')
    return max
