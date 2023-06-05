def solve(n):
    res = 0
    for i in range(1, n):
        res += (n - 1) // i
    return res

if __name__ == '__main__':
    solve()