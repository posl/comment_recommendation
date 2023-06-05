def min_sadness(n, a):
    min_sadness = 0
    sum_a = sum(a)
    sum_b = 0
    for i in range(n):
        sum_b += a[i]
        min_sadness += abs(sum_a - sum_b)
    return min_sadness

if __name__ == '__main__':
    min_sadness()