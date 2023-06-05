def solve(n, a):
    ans = 0
    cnt = [0] * (10 ** 6 + 1)
    for i in range(n):
        ans += i - cnt[a[i]]
        cnt[a[i]] += 1
    return ans

if __name__ == '__main__':
    solve()