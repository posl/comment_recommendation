def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    
    #累積和を計算
    S = [0]
    for i in range(N):
        S.append(S[-1] + p[i])
    
    #K個選んだ時の期待値の最大値を求める
    ans = 0
    for i in range(N-K+1):
        ans = max(ans, (S[i+K] - S[i])/2 + S[i])
    
    print(ans)

if __name__ == '__main__':
    solve()