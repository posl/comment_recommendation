def solve(n, a):
    ans = 0
    minus = 0
    min_abs = 10**9
    for i in range(n):
        if a[i] < 0:
            minus += 1
        ans += abs(a[i])
        min_abs = min(min_abs, abs(a[i]))
    if minus % 2 == 0:
        return ans
    else:
        return ans - 2 * min_abs

if __name__ == '__main__':
    solve()