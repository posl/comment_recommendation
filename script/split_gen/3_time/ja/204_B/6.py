def harvest(n,a):
    result = 0
    for i in range(n):
        if a[i] > 10:
            result += a[i] - 10
    return result
