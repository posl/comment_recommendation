def solve():
    N,W = map(int,input().split())
    S = [0]*N
    T = [0]*N
    P = [0]*N
    for i in range(N):
        S[i],T[i],P[i] = map(int,input().split())
    #print(S,T,P)
    #時刻ごとに、その時刻にお湯を使う人の数をカウント
    #時刻 0 から 2×10^5 まで
    count = [0]*(2*10**5+1)
    for i in range(N):
        count[S[i]] += P[i]
        count[T[i]] -= P[i]
    #print(count)
    #時刻ごとに、その時刻にお湯を使う人の数を累積和
    for i in range(1,len(count)):
        count[i] += count[i-1]
    #print(count)
    #時刻ごとに、その時刻にお湯を使う人の数が、給湯器の容量を超えているかチェック
    for i in range(len(count)):
        if count[i] > W:
            print("No")
            return
    print("Yes")
