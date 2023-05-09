def solve():
    N, M = map(int, input().split())
    mod = 10**9+7
    ans = 1
    for i in range(2, int(M**0.5)+1):
        cnt = 0
        while M % i == 0:
            M = M // i
            cnt += 1
        ans = ans * (cnt + N) % mod
    if M != 1:
        ans = ans * (N + 1) % mod
    print(ans)

if __name__ == '__main__':
    solve()