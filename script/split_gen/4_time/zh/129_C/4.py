def climb_stairs(n, a):
    stairs = [0] * (n + 1)
    stairs[0] = 1
    for i in range(1, n + 1):
        for j in range(len(a)):
            if i - a[j] >= 0:
                stairs[i] += stairs[i - a[j]]
                stairs[i] %= 1000000007
    return stairs[n]
