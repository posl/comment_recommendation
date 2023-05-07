def main():
    #入力
    N, K = map(int, input().split())
    S = input()
    #初期値
    ans = 0
    #0 から N-1 までの各 i について、
    #i から左に向かって連続する L の数を Lcnt[i] とする。
    Lcnt = [0] * N
    #i から右に向かって連続する R の数を Rcnt[i] とする。
    Rcnt = [0] * N
    #Lcnt, Rcnt を求める
    for i in range(N):
        if S[i] == "L":
            if i == 0:
                Lcnt[i] = 1
            else:
                Lcnt[i] = Lcnt[i-1] + 1
        else:
            Lcnt[i] = 0
    for i in range(N-1, -1, -1):
        if S[i] == "R":
            if i == N-1:
                Rcnt[i] = 1
            else:
                Rcnt[i] = Rcnt[i+1] + 1
        else:
            Rcnt[i] = 0
    #0 から N-1 までの各 i について、
    #i から左に向かって連続する L の数が K より大きいならば、
    #Lcnt[i] + Rcnt[i] が答えである。
    #そうでないならば、Lcnt[i] + Rcnt[i] - 1 が答えである。
    for i in range(N):
        if Lcnt[i] > K:
            ans = max(ans, Lcnt[i] + Rcnt[i])
        else:
            ans = max(ans, Lcnt[i] + Rcnt[i] - 1)
    #出力
    print(ans)
