def min_sadness(n, a):
    a.sort()
    b = a[0] - 1
    min_sad = 0
    for i in range(1, n):
        min_sad += abs(a[i] - (b + i))
    return min_sad
