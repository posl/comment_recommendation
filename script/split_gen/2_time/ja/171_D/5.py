def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    S = [0] * (Q + 1)
    S[0] = sum(A)
    B = [0] * (N + 1)
    for i in range(N):
        B[A[i]] += 1
    for i in range(Q):
        S[i + 1] = S[i] + (BC[i][1] - BC[i][0]) * B[BC[i][0]]
        B[BC[i][1]] += B[BC[i][0]]
        B[BC[i][0]] = 0
    for i in range(Q):
        print(S[i + 1])
