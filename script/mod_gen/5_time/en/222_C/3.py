def main():
    N, M = map(int, input().split())
    A = []
    for i in range(2 * N):
        A.append(input())
    B = []
    for i in range(2 * N):
        B.append([0, i + 1])
    for i in range(M):
        for j in range(N):
            a = B[2 * j][1] - 1
            b = B[2 * j + 1][1] - 1
            if A[a][i] == A[b][i]:
                continue
            if A[a][i] == 'G' and A[b][i] == 'C':
                B[2 * j][0] += 1
            elif A[a][i] == 'C' and A[b][i] == 'P':
                B[2 * j][0] += 1
            elif A[a][i] == 'P' and A[b][i] == 'G':
                B[2 * j][0] += 1
            else:
                B[2 * j + 1][0] += 1
        B.sort(key=lambda x: (-x[0], x[1]))
    for i in range(2 * N):
        print(B[i][1])

if __name__ == '__main__':
    main()