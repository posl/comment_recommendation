def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    ans[a[0]] = 1
    for i in range(1, n):
        na = [0] * 10
        for j in range(10):
            na[(j + a[i]) % 10] += ans[j]
            na[(j * a[i]) % 10] += ans[j]
            na[(j + a[i]) % 10] %= mod
            na[(j * a[i]) % 10] %= mod
        ans = na
    print(*ans, sep="\n")

if __name__ == '__main__':
    solve()