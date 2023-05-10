def solve(n):
    i = 1
    ans = 0
    while i * (i + 1) <= 2 * n:
        if (2 * n + i - i * i) % (2 * i) == 0:
            ans += 1
        i += 1
    return ans * 2
