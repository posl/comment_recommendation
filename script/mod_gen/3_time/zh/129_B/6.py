def min_diff(n, w):
    min_diff = 100000
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    return min_diff

if __name__ == '__main__':
    min_diff()