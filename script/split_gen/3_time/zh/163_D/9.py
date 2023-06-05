def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    ans = 0
    for i in range(K, N+2):
        min = (i-1)*i//2
        max = (2*N-i+1)*i//2
        ans += max - min + 1
        ans %= mod
    print(ans)
