def solve():
    n = int(input())
    c = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 1
    for i in range(n):
        ans *= min(i + 1, c[i])
        ans %= mod
    print(ans)
