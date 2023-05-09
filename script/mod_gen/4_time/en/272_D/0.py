def main():
    N, M = map(int, input().split())
    ret = [[-1 for j in range(N)] for i in range(N)]
    ret[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ret[i][j] == -1:
                continue
            for k in range(N):
                for l in range(N):
                    if (i-k)**2+(j-l)**2 == M:
                        ret[k][l] = ret[i][j]+1
    for i in range(N):
        print(' '.join(map(str, ret[i])))

if __name__ == '__main__':
    main()