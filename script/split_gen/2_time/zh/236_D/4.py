def xor_sum(a):
    x = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            x += a[i][j]
    return x
