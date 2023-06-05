def max_expected_value(n, k, p):
    s = sum(p[0:k])
    max_s = s
    for i in range(k, n):
        s += p[i] - p[i-k]
        max_s = max(max_s, s)
    return (max_s + k) / 2

if __name__ == '__main__':
    max_expected_value()