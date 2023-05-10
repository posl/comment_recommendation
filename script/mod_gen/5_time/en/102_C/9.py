def solve(n, a):
    a.sort()
    b = [0] * n
    for i in range(n):
        b[i] = a[i] - (i + 1)
    b.sort()
    if n % 2 == 1:
        med = b[n // 2]
    else:
        med = (b[n // 2] + b[n // 2 - 1]) // 2
    ans = 0
    for i in range(n):
        ans += abs(b[i] - med)
    return ans

if __name__ == '__main__':
    solve()