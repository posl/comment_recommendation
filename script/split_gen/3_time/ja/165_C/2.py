def main():
    N, M, Q = map(int, input().split())
    A = [0] * Q
    B = [0] * Q
    C = [0] * Q
    D = [0] * Q
    for i in range(Q):
        A[i], B[i], C[i], D[i] = map(int, input().split())
    ans = 0
    for i in range(1, M + 1):
        A = [i]
        for j in range(2, N + 1):
            for k in range(A[j - 2], M + 1):
                A.append(k)
                for l in range(Q):
                    if A[B[l] - 1] - A[A[l] - 1] == C[l]:
                        ans += D[l]
    print(ans)
