def solve():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    ans = 0
    power3 = 1
    for i in range(N-1, -1, -1):
        if S[i] == 'C':
            ans += power3
            ans %= MOD
        elif S[i] == '?':
            ans *= 3
            ans %= MOD
            power3 *= 3
            power3 %= MOD
        else:
            pass
    print(ans)
solve()
