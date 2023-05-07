def main():
    # Read input
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    # Solve
    B = [0] * N
    for i in range(K):
        B[A[i]-1] = i+1
    for i in range(Q):
        if B[L[i]-1] == 0:
            continue
        if L[i] == N:
            continue
        if B[L[i]] != 0:
            continue
        B[L[i]-1], B[L[i]] = B[L[i]], B[L[i]-1]
    # Print output
    for i in range(N):
        print(B[i], end=' ')
    print()

if __name__ == '__main__':
    main()