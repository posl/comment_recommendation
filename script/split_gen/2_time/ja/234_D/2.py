def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]
    C = [0] * N
    for p in P:
        C[p] += 1
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + C[i]
    for i in range(K, N):
        print(S[P[i]] - S[P[i - K]])
