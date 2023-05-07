def min_sadness(a):
    b = sum(a) // len(a)
    return sum(abs(a[i] - (b + i + 1)) for i in range(len(a)))
