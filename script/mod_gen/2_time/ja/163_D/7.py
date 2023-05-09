def main():
    # 入力
    N, K = map(int, input().split())
    
    # 10^9+7
    mod = 10**9+7
    
    # 答え
    ans = 0
    
    # 答えを求める
    for i in range(K, N+2):
        # 1~iの総和
        sum1 = i*(i+1)//2
        # N~N-i+1の総和
        sum2 = (N-i+1)*N//2 + (N-i+1)
        # 答えに加算
        ans = (ans + sum1 - sum2 + 1) % mod
    
    # 出力
    print(ans)

if __name__ == '__main__':
    main()