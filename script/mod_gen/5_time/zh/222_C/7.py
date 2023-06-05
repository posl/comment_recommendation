def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2 * N)]
    rank = [[i + 1, 0] for i in range(2 * N)]
    for i in range(M):
        for j in range(N):
            k = 2 * j
            if (A[rank[k][0] - 1][i] == "G" and A[rank[k + 1][0] - 1][i] == "C") or (A[rank[k][0] - 1][i] == "C" and A[rank[k + 1][0] - 1][i] == "P") or (A[rank[k][0] - 1][i] == "P" and A[rank[k + 1][0] - 1][i] == "G"):
                rank[k][1] += 1
            elif (A[rank[k][0] - 1][i] == "C" and A[rank[k + 1][0] - 1][i] == "G") or (A[rank[k][0] - 1][i] == "P" and A[rank[k + 1][0] - 1][i] == "C") or (A[rank[k][0] - 1][i] == "G" and A[rank[k + 1][0] - 1][i] == "P"):
                rank[k + 1][1] += 1
        rank.sort(key=lambda x: x[1], reverse=True)
    for i in range(2 * N):
        print(rank[i][0])

if __name__ == '__main__':
    main()