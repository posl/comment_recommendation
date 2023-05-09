def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 前処理
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 1つ目の分割
    min_diff = 10 ** 9
    for i in range(1, N - 1):
        P = S[i]
        min_Q = 10 ** 9
        for j in range(i + 1, N):
            Q = S[j] - S[i]
            min_Q = min(min_Q, Q)
            R = S[N] - S[j]
            min_diff = min(min_diff, max(P, Q, R) - min(P, Q, R))
        # 2つ目の分割
        for j in range(i + 1, N):
            Q = S[j] - S[i]
            R = S[N] - S[j]
            min_diff = min(min_diff, max(P, Q, R) - min(P, Q, R))
    print(min_diff)
