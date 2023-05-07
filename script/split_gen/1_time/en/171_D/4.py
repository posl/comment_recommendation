def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = [int(x) for x in input().split()]
    S = 0
    for i in range(N):
        S += A[i]
    for i in range(Q):
        S -= B[i] * A.count(B[i])
        S += C[i] * A.count(B[i])
        print(S)
