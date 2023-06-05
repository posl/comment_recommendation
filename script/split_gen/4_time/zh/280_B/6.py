def solve(n, s):
    sum_s = sum(s)
    sum_a = 0
    a = [0] * n
    for i in range(n):
        if i % 2 == 0:
            a[i] = max(-sum_a, sum_s - sum_a)
        else:
            a[i] = -max(-sum_a, sum_s - sum_a)
        sum_a += a[i]
    return a
