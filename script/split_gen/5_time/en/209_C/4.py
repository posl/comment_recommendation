def problems209_c():
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10**9+7
    C.sort()
    ans = 1
    for i in range(N):
        ans *= max(C[i]-i, 0)
        ans %= MOD
    print(ans)
