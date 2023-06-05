def get_min_sadness(n, a):
    b = 0
    min_sadness = 0
    for i in range(n):
        min_sadness += abs(a[i] - (b + i + 1))
    return min_sadness

if __name__ == '__main__':
    get_min_sadness()