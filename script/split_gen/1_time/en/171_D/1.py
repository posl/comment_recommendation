def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    S = sum(A)
    for i in range(Q):
        S += (C[i] - B[i]) * A.count(B[i])
        print(S)
