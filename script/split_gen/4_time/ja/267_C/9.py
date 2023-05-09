def max_sum(n, m, a):
    sums = [0] * (n+1)
    for i in range(n):
        sums[i+1] = sums[i] + a[i]
    maxs = 0
    for i in range(n-m+1):
        maxs = max(maxs, sums[i+m] - sums[i] + (m*(m+1)//2))
    return maxs
