def solve(n, x, y):
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(y[i] - y[j]) <= abs(x[i] - x[j]):
                res += 1
    return res

if __name__ == '__main__':
    solve()