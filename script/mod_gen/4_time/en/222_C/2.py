def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    B = [[0, i+1] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            a, b = B[2*j][1]-1, B[2*j+1][1]-1
            if A[a][i] == A[b][i]:
                continue
            elif A[a][i] == 'G':
                if A[b][i] == 'C':
                    B[2*j][0] += 1
                else:
                    B[2*j+1][0] += 1
            elif A[a][i] == 'C':
                if A[b][i] == 'P':
                    B[2*j][0] += 1
                else:
                    B[2*j+1][0] += 1
            else:
                if A[b][i] == 'G':
                    B[2*j][0] += 1
                else:
                    B[2*j+1][0] += 1
        B.sort(key=lambda x: (-x[0], x[1]))
    for b in B:
        print(b[1])

if __name__ == '__main__':
    main()