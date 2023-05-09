def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if (i+j)%2 == 0:
                if B[i][j] != 1:
                    print('No')
                    return
            else:
                if B[i][j] != 2:
                    print('No')
                    return
    print('Yes')

if __name__ == '__main__':
    main()