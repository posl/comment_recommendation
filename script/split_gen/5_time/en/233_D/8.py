def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # Aの累積和
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    # 累積和の差分
    T = []
    for i in range(N+1):
        T.append(S[i] - K)
    # 累積和の差分の集合
    T = set(T)
    # 累積和の差分の集合に含まれる累積和の個数をカウント
    count = 0
    for i in range(N+1):
        if S[i] in T:
            count += 1
    print(count)
