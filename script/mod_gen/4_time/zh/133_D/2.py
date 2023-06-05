def solve(n, a):
    ans = [0] * n
    for i in range(n):
        ans[i] = a[i] * 2
    for i in range(n):
        ans[i] -= ans[(i + 1) % n] + ans[(i - 1) % n]
    return ans

if __name__ == '__main__':
    solve()