def solve():
    N, M = map(int, input().split())
    A = [input() for _ in range(2 * N)]
    rank = [[i + 1, 0] for i in range(2 * N)]
    for i in range(M):
        for j in range(N):
            id1 = rank[2 * j][0] - 1
            id2 = rank[2 * j + 1][0] - 1
            if A[id1][i] == A[id2][i]:
                continue
            elif A[id1][i] == 'G' and A[id2][i] == 'C':
                rank[2 * j][1] -= 1
            elif A[id1][i] == 'C' and A[id2][i] == 'P':
                rank[2 * j][1] -= 1
            elif A[id1][i] == 'P' and A[id2][i] == 'G':
                rank[2 * j][1] -= 1
            else:
                rank[2 * j + 1][1] -= 1
        rank.sort(key=lambda x: (x[1], x[0]))
    for i in range(2 * N):
        print(rank[i][0])
solve()
