def main():
    mod = 10**9 + 7
    N, K = map(int, input().split())
    for i in range(1, K+1):
        print((comb(N-K+1, i, mod) * comb(K-1, i-1, mod)) % mod)
