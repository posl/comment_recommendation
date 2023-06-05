def get_min_permutation(n, p):
    p = [int(x) for x in p.split()]
    k = 0
    for i in range(n):
        k += (p[i] - 1) * factorial(n - i - 1)
    k += 1
    q = [0] * n
    used = [False] * n
    for i in range(n):
        for j in range(n):
            if used[j]:
                continue
            q[i] = j + 1
            if factorial(n - i - 1) < k:
                k -= factorial(n - i - 1)
            else:
                used[j] = True
                break
    return q
