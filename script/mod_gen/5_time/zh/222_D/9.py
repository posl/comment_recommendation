def problem222_d():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    ans = 1
    for i in range(n):
        ans *= max(b[i] - a[i] + 1, 0)
        ans %= mod
    print(ans)
problem222_d()
