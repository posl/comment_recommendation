def get_max_sum(n, m, a):
    if n < m:
        return None
    if n == m:
        return sum([i * a[i] for i in range(1, n + 1)])
    else:
        max_sum = 0
        for i in range(n - m + 1):
            tmp_sum = sum([j * a[i + j] for j in range(1, m + 1)])
            if tmp_sum > max_sum:
                max_sum = tmp_sum
        return max_sum

if __name__ == '__main__':
    get_max_sum()