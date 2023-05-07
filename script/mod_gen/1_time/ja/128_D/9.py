def main():
    #入力
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    
    #計算
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1):
            if i + j > K or i + j > N:
                continue
            w = V[:i] + V[N - j:]
            w.sort()
            w = w[:K - i - j]
            ans = max(ans, sum(w) + i + j)
    
    #出力
    print(ans)

if __name__ == '__main__':
    main()