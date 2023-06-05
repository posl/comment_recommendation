def solve(n):
    ans = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i * j <= n and i * i != j * j:
                ans += 2
            elif i * j <= n and i * i == j * j:
                ans += 1
    return ans
