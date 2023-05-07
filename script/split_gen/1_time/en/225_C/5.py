def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for i in range(N)]
    for i in range(10**4):
        for j in range(7):
            if A[i][j] == B[0][0]:
                if (i+N) <= 10**4 and (j+M) <= 7:
                    for k in range(N):
                        for l in range(M):
                            if A[i+k][j+l] != B[k][l]:
                                break
                        else:
                            continue
                        break
                    else:
                        print('Yes')
                        return
    print('No')
