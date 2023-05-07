def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = [int(j) for j in input().split()]
    S = sum(A)
    for i in range(Q):
        S += (C[i] - B[i]) * A.count(B[i])
        print(S)
