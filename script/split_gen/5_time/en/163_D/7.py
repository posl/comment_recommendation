def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    if N == K:
        print(1)
        exit()
    if K == 1:
        print((N+1)*(N+1))
        exit()
    ans = 0
    for i in range(K, N+2):
        ans += i*(N+1-i+1) + 1
        ans %= MOD
    print(ans)
