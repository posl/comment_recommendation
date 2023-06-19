def main():
    N, K = map(int, input().split())
    mod = 10 ** 9 + 7
    if N == K - 1:
        print(1)
    else:
        ans = 0
        for i in range(K, N + 2):
            ans += (N + 1) * i - i * (i - 1) // 2 + 1
            ans %= mod
        print(ans)
