def solve(X, M):
    d = int(max(X))
    n = 0
    for i in range(1, len(X) + 1):
        n += int(X[-i]) * pow(d + 1, i - 1)
    ans = 0
    while n <= M:
        ans += 1
        n += pow(d + 1, len(X) - 1)
    return ans
