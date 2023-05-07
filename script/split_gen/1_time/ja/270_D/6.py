def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    #初期化
    dp = [0] * (N+1)
    dp[1] = 1
    #dp[i] = iを取るときの勝ち負け
    #dp[i] = 0:負け
    #dp[i] = 1:勝ち
    for i in range(2,N+1):
        for j in range(K):
            if A[j] > i:
                break
            if dp[i-A[j]] == 0:
                dp[i] = 1
                break
    if dp[N] == 1:
        print("Takahashi")
    else:
        print("Aoki")
