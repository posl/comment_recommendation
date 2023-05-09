def main():
    #入力
    N,K = map(int,input().split())
    h = [int(input()) for i in range(N)]
    #ソート
    h.sort()
    #答え
    ans = 10**9
    #高さの差の最小値を求める
    for i in range(N-K+1):
        ans = min(ans,h[i+K-1]-h[i])
    #出力
    print(ans)
