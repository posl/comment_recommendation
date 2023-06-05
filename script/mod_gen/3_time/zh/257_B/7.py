def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    B = [0 for i in range(N)]
    for i in range(K):
        B[A[i] - 1] += 1
    for i in range(N):
        B[i] = 1 if B[i] > 0 else 0
    for i in range(Q):
        if B[L[i] - 1] == 0:
            continue
        elif L[i] == N:
            continue
        elif B[L[i]] == 0:
            B[L[i]] = 1
            B[L[i] - 1] = 0
        else:
            continue
    for i in range(N):
        if B[i] == 1:
            print(i + 1, end=' ')
    print()

if __name__ == '__main__':
    main()