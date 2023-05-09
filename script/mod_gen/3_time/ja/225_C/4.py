def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    A = [[(i - 1) * 7 + j for j in range(1, 8)] for i in range(1, 10 ** 100 + 1)]
    for i in range(len(A) - N + 1):
        for j in range(len(A[i]) - M + 1):
            if A[i][j] == B[0][0]:
                for k in range(N):
                    for l in range(M):
                        if A[i + k][j + l] != B[k][l]:
                            break
                    else:
                        continue
                    break
                else:
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()