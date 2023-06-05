def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * (2**(N - 1))
    print(ans % 998244353)
solve()
