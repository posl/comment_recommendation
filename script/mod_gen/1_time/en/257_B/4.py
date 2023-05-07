def solve():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #print(N, K, Q)
    #print(A)
    #print(L)
    B = [0] * N
    for i in range(K):
        B[A[i] - 1] = i + 1
    #print(B)
    for i in range(Q):
        l = L[i] - 1
        if B[l] == 0:
            continue
        if l == 0:
            if B[l + 1] == 0:
                B[l], B[l + 1] = B[l + 1], B[l]
        elif l == N - 1:
            if B[l - 1] == 0:
                B[l], B[l - 1] = B[l - 1], B[l]
        else:
            if B[l - 1] == 0:
                B[l], B[l - 1] = B[l - 1], B[l]
            elif B[l + 1] == 0:
                B[l], B[l + 1] = B[l + 1], B[l]
    for i in range(N):
        if B[i] == 0:
            continue
        else:
            print(i + 1, end = ' ')
    print()

if __name__ == '__main__':
    solve()