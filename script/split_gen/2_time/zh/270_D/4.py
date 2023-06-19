def solve(n, k, a):
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + 1
        for j in range(k):
            if i - a[j] < 0:
                break
            s[i] = min(s[i], s[i - a[j]])
        s[i] = s[i] + 1
    return s[n]
