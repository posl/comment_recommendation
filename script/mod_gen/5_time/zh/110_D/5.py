def solve(N,M):
    mod = 10**9+7
    ans = 1
    i = 2
    while i*i <= M:
        cnt = 0
        while M%i == 0:
            cnt += 1
            M //= i
        ans = (ans * comb(N+cnt-1, cnt, mod)) % mod
        i += 1
    if M != 1:
        ans = (ans * N) % mod
    return ans

if __name__ == '__main__':
    solve()