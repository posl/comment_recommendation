def solve(n, a):
    ans = [0] * n
    for i in range(1, n):
        ans[a[i - 1] - 1] += 1
    return ans

if __name__ == '__main__':
    solve()