def main():
    N, M, K = map(int, input().split())
    ans = 0
    for i in range(M):
        ans += (i+1)*pow(M, N-1, 998244353)
    ans *= pow(M, K-N, 998244353)
    print(ans%998244353)
