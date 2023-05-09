def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # 累積和をとる
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 各 X について、
    # (1) X 以下の要素の和を S から取り出す
    # (2) X 以上の要素の和を S から取り出す
    # (3) 1 と 2 の差
    # を計算し、それをすべて足したものが答え
    for x in X:
        ans = 0
        for i in range(N + 1):
            ans += min(S[i], x) * i - S[i]
        print(ans)
