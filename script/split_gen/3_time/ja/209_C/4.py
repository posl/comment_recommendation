def solve():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    mod = 10**9 + 7
    ans = 1
    for i in range(N):
        ans *= C[i] - i
        ans %= mod
    print(ans)
