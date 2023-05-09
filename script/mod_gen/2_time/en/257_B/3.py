def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #print(N, K, Q)
    #print(A)
    #print(L)
    B = [0] * (N+1)
    for i in range(K):
        B[A[i]] = i + 1
    #print(B)
    for i in range(Q):
        if B[L[i]] == 0:
            continue
        else:
            if B[L[i]] == 1:
                continue
            else:
                B[L[i]-1], B[L[i]] = B[L[i]], B[L[i]-1]
    for i in range(1, N+1):
        if B[i] == 0:
            print(i, end=" ")
        else:
            print(A[B[i]-1], end=" ")
    print()

if __name__ == '__main__':
    main()