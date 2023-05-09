def main():
    #入力
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    #P,Q,Rの最大値を求める
    maxP = 0
    maxQ = 0
    maxR = 0
    for i in range(N):
        maxP = max(maxP, S[i + 1] - S[0])
        maxQ = max(maxQ, S[i + 1] - S[max(0, i - P + 1)])
        maxR = max(maxR, S[i + 1] - S[max(0, i - Q + 1)])
    #条件を満たす組が存在するか判定
    for i in range(N):
        if (S[i + 1] - S[max(0, i - R + 1)]) == maxR:
            print("Yes")
            return
    print("No")
    return
