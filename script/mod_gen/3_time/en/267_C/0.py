def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    D = {}
    for i in range(N + 1):
        if B[i] % M in D:
            D[B[i] % M].append(i)
        else:
            D[B[i] % M] = [i]
    ans = 0
    for i in range(M):
        if i in D:
            for j in range(len(D[i]) - 1):
                ans = max(ans, (D[i][j + 1] - D[i][j]) // M)
    print(ans * M)

if __name__ == '__main__':
    main()