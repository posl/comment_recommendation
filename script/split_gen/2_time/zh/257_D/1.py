def solve(num, x, y, p):
    ans = 0
    for i in range(num):
        for j in range(num):
            if i == j:
                continue
            if p[i] * ans >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                ans += 1
                break
    return ans
