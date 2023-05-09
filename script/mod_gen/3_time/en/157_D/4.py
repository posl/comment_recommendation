def main():
    N, M, K = list(map(int, input().split()))
    friend = [[0 for i in range(N)] for j in range(N)]
    block = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        a, b = list(map(int, input().split()))
        friend[a - 1][b - 1] = 1
        friend[b - 1][a - 1] = 1
    for i in range(K):
        c, d = list(map(int, input().split()))
        block[c - 1][d - 1] = 1
        block[d - 1][c - 1] = 1
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i == j:
                continue
            if friend[i][j] == 1:
                cnt += 1
        for j in range(N):
            if block[i][j] == 1:
                cnt += 1
        print(N - cnt - 1, end = " ")

if __name__ == '__main__':
    main()