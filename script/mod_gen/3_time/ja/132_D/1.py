def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    for i in range(1, K+1):
        # 青いボールをi個取る方法の数
        blue = comb(K-1, i-1)
        # 赤いボールをi個取る方法の数
        red = comb(N-K+1, i)
        print(blue * red % MOD)

if __name__ == '__main__':
    main()