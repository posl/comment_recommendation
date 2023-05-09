def main():
    #入力
    N = int(input())
    W = list(map(int, input().split()))
    #初期化
    S = [0]
    for i in range(N):
        S.append(S[i] + W[i])
    #print(S)
    #差の絶対値の最小値を求める
    ans = float("inf")
    for i in range(1,N):
        ans = min(ans, abs(S[i] - (S[N] - S[i])))
    #出力
    print(ans)
