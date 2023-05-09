def main():
    N, K, Q = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    L = [int(x) for x in input().split()]
    B = [0] * N
    for i in range(K):
        B[A[i] - 1] = i + 1
    for i in range(Q):
        if B[L[i] - 1] > 0:
            if L[i] < N:
                if B[L[i]] == 0:
                    B[L[i] - 1] = 0
                    B[L[i]] = L[i]
                    L[i] += 1
            else:
                B[L[i] - 1] = 0
        else:
            pass
    for i in range(N):
        if B[i] > 0:
            print(B[i], end = " ")
        else:
            print(i + 1, end = " ")
    print()
