def main():
    N, K, Q = map(int, input().split())
    A = [int(i) for i in input().split()]
    L = [int(i) for i in input().split()]
    B = [0] * N
    for i in range(K):
        B[A[i] - 1] += 1
    for i in range(N):
        if B[i] > 0:
            B[i] = 1
    for i in range(N - 1):
        B[i + 1] += B[i]
    for i in range(Q):
        print(B[L[i] - 1])

if __name__ == '__main__':
    main()