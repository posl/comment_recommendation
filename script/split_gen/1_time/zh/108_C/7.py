def solve(n, k):
    ans = 0
    for i in range(1, n + 1):
        if i % k == 0:
            ans += 1
        else:
            ans += 2
    return ans
