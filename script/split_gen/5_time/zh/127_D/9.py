def max_card(n, m, a, b, c):
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        if b[i] >= n:
            sum += c[i] * n
            return sum
        else:
            sum += c[i] * b[i]
            n -= b[i]
    sum += a[0] * n
    return sum
