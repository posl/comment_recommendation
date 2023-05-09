def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #累積和を作成
    S = [0] * (N+1)
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i-1]
    #累積和の差分がKとなる組の数をカウント
    from collections import defaultdict
    D = defaultdict(int)
    ans = 0
    for i in range(N+1):
        ans += D[S[i] - K]
        D[S[i]] += 1
    
    print(ans)

if __name__ == '__main__':
    main()