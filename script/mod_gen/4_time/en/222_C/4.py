def main():
    N, M = map(int, input().split())
    A = [input() for i in range(2*N)]
    r = [[i, 0] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            a = r[2*j][0]
            b = r[2*j+1][0]
            if A[a][i] == A[b][i]:
                continue
            elif A[a][i] == 'G':
                if A[b][i] == 'C':
                    r[2*j][1] -= 1
                else:
                    r[2*j+1][1] -= 1
            elif A[a][i] == 'C':
                if A[b][i] == 'P':
                    r[2*j][1] -= 1
                else:
                    r[2*j+1][1] -= 1
            else:
                if A[b][i] == 'G':
                    r[2*j][1] -= 1
                else:
                    r[2*j+1][1] -= 1
        r.sort(key=lambda x: x[1])
    for i in range(2*N):
        print(r[i][0]+1)

if __name__ == '__main__':
    main()