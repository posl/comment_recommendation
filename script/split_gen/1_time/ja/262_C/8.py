def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    #Aの値をkeyとした辞書を作成
    D = {i:[] for i in range(1,N+1)}
    for i in range(N):
        D[A[i]].append(i)
    #Aの値をkeyとした辞書から
    #最小値と最大値のindexを取得
    min_idx = [0]*N
    max_idx = [0]*N
    for i in range(1,N+1):
        min_idx[i-1] = D[i][0]
        max_idx[i-1] = D[i][-1]
    #min_idxの累積和を取得
    cumsum_min = [0]*(N+1)
    for i in range(1,N+1):
        cumsum_min[i] = cumsum_min[i-1] + min_idx[i-1]
    #max_idxの累積和を取得
    cumsum_max = [0]*(N+1)
    for i in range(1,N+1):
        cumsum_max[i] = cumsum_max[i-1] + max_idx[i-1]
    #min_idxとmax_idxを使って
    #条件を満たすi, jの組の数を求める
    ans = 0
    for i in range(1,N+1):
        ans += cumsum_max[i] - cumsum_max[i-1] * i
        ans += cumsum_min[N] - cumsum_min[i] - (N-i) * max_idx[i-1]
    print(ans)
