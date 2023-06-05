def solve(n, a):
    ans = 0
    while True:
        ok = True
        for i in range(n):
            if a[i] % 2 == 1:
                ok = False
        if not ok:
            break
        for i in range(n):
            a[i] = a[i] // 2
        ans += 1
    return ans

if __name__ == '__main__':
    solve()