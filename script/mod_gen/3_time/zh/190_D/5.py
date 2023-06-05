def solve(n):
    ans = 0
    s = 0
    for i in range(1, n+1):
        s += i
        if s >= n:
            break
    if s == n:
        ans += 1
    for i in range(1, n+1):
        s -= i
        s += (i+n)
        if s >= n:
            break
        if (s-n) % 2 == 0:
            ans += 1
    return ans

if __name__ == '__main__':
    solve()