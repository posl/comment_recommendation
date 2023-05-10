def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    A = [0] + A
    S = sum(A)
    D = {}
    for i in range(1, N+1):
        D[i] = A[i]
    for b, c in BC:
        S += (c - b) * D[b]
        D[c] += D[b]
        D[b] = 0
        print(S)
