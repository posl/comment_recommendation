def main():
    N, M, K = map(int, input().split())
    relation = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        relation[a-1][b-1] = 1
        relation[b-1][a-1] = 1
    for _ in range(K):
        c, d = map(int, input().split())
        relation[c-1][d-1] = 2
        relation[d-1][c-1] = 2
    for i in range(N):
        count = 0
        for j in range(N):
            if i != j and relation[i][j] == 0:
                for k in range(N):
                    if relation[i][k] == 1 and relation[j][k] == 1:
                        count += 1
                        break
        print(count)

if __name__ == '__main__':
    main()