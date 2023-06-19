def get_sum(a):
    sum = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            sum += a[i][j]
    return sum
