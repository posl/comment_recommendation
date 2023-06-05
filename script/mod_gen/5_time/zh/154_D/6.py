def max_expected_value(n, k, p):
    p_sum = sum(p[0:k])
    max_sum = p_sum
    for i in range(k, n):
        p_sum += p[i] - p[i-k]
        if p_sum > max_sum:
            max_sum = p_sum
    return (max_sum + k)/2

if __name__ == '__main__':
    max_expected_value()