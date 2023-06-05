def main():
    N, M, Q = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    P = [0] * Q
    Q = [0] * Q
    for i in range(Q):
        P[i], Q[i] = map(int, input().split())
    for i in range(Q):
        count = 0
        for j in range(M):
            if (L[j] >= P[i] and R[j] <= Q[i]):
                count += 1
        print(count)
