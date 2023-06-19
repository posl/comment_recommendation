def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))
    B = A.copy()
    for i in range(P-1, Q):
        B[i] = A[i+R-Q]
    for i in range(R-1, S):
        B[i] = A[i+P-R]
    for i in range(N):
        print(B[i], end=' ')
    print()

if __name__ == '__main__':
    main()