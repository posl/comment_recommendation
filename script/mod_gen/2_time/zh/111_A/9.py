def solve():
    #N,M = map(int, input().split())
    N,M = 100000, 1000000000
    mod = 1000000007
    ans = 1
    i = 2
    while i * i <= M:
        cnt = 0
        while M % i == 0:
            cnt += 1
            M //= i
        ans = ans * (cnt + N - 1) % mod
        i += 1
    if M != 1:
        ans = ans * N % mod
    print(ans)

if __name__ == '__main__':
    solve()