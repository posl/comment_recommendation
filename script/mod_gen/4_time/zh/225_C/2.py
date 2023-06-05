def main():
    N, M = map(int, input().split())
    B = []
    for i in range(N):
        B.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(M):
            B[i][j] -= (i) * 7 + (j + 1)
    for j in range(M):
        for i in range(1, N):
            if B[i][j] <= B[i - 1][j]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()