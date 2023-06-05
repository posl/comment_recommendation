def main():
    N, M = map(int, input().split())
    #N, M = 100000, 1000000000
    mod = 10**9+7
    ans = 1
    i = 2
    while i*i <= M:
        if M % i == 0:
            cnt = 0
            while M % i == 0:
                cnt += 1
                M //= i
            ans *= comb(N+cnt-1, cnt, mod)
            ans %= mod
        i += 1
    if M != 1:
        ans *= N
        ans %= mod
    print(ans)
