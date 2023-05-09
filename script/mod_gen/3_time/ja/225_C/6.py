def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    A = [[0] * 7 for _ in range(10 ** 4)]
    for i in range(10 ** 4):
        for j in range(7):
            A[i][j] = (i) * 7 + j + 1
    flag = False
    for i in range(10 ** 4 - N + 1):
        for j in range(7 - M + 1):
            if A[i][j] == B[0][0]:
                for k in range(N):
                    for l in range(M):
                        if A[i + k][j + l] != B[k][l]:
                            break
                    else:
                        continue
                    break
                else:
                    flag = True
                    break
        else:
            continue
        break
    print('Yes' if flag else 'No')

if __name__ == '__main__':
    main()