def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 累積和を求める
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    # 3箇所で切るので、全ての切り方を試す
    ans = 10**9
    for i in range(1, N-1):
        for j in range(i+1, N):
            # P,Q,R,Sを求める
            P = S[i]
            Q = S[j]-S[i]
            R = S[N]-S[j]
            S_max = max(P, Q, R)
            S_min = min(P, Q, R)
            # 最大値と最小値の差を更新する
            ans = min(ans, S_max-S_min)
    print(ans)
