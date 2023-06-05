def solve(h, w, c, a):
    ans = 10**18
    for i in range(h):
        for j in range(w):
            for i2 in range(h):
                for j2 in range(w):
                    if i == i2 and j == j2:
                        continue
                    cost = a[i][j] + a[i2][j2] + c * (abs(i - i2) + abs(j - j2))
                    ans = min(ans, cost)
    return ans
