def main():
    import sys
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # A = list(map(int, sys.stdin.read().split()))
    # N, M = A[0], A[1]
    # A = A[2:]
    B = [0] * (N - M + 1)
    for i in range(N - M + 1):
        for j in range(M):
            B[i] += (j + 1) * A[i + j]
    print(max(B))

if __name__ == '__main__':
    main()