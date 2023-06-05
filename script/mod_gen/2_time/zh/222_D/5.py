def solve():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    rank = [[i+1, 0, 0] for i in range(2*N)]
    for m in range(M):
        for i in range(N):
            a1 = A[rank[2*i][0]-1][m]
            a2 = A[rank[2*i+1][0]-1][m]
            if a1 == a2:
                continue
            if a1 == 'G':
                if a2 == 'C':
                    rank[2*i][1] += 1
                else:
                    rank[2*i+1][1] += 1
            elif a1 == 'C':
                if a2 == 'G':
                    rank[2*i+1][1] += 1
                else:
                    rank[2*i][1] += 1
            else:
                if a2 == 'G':
                    rank[2*i][1] += 1
                else:
                    rank[2*i+1][1] += 1
        rank.sort(key=lambda x: (-x[1], x[2], x[0]))
        for i in range(2*N):
            rank[i][2] = i
    for i in range(2*N):
        print(rank[i][0])

if __name__ == '__main__':
    solve()