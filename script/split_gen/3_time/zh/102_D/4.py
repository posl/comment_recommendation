def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 二分探索
    ans = float("inf")
    for i in range(2, N - 1):
        # P, Q, R, S の候補のうち、最大値と最小値の差が最小になるものを求める
        # P, Q, R, S の候補は、S[1:i], S[i:j], S[j:k], S[k:N] となる
        # 二分探索を行うために、S[i:j] の値が S[1:i] から最も近い値を二分探索で求める
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の値と S[i:j] の値の差の最小値となる
        # 二分探索で求めた値が S[1:i] の
