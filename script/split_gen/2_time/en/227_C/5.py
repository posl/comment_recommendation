def solve(n):
    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        for j in range(i, int(n ** 0.5) + 1):
            for k in range(j, int(n ** 0.5) + 1):
                if i * j * k <= n:
                    ans += 1
                else:
                    break
    return ans
