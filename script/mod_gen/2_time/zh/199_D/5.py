def solve(n, m, a, b):
    ans = 0
    for i in range(3 ** n):
        ok = True
        for j in range(m):
            if i >> (a[j] - 1) % 3 == i >> (b[j] - 1) % 3:
                ok = False
        if ok:
            ans += 1
    return ans

if __name__ == '__main__':
    solve()