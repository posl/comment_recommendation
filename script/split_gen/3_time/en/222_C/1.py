def main():
    N, M = map(int, input().split())
    A = [input() for i in range(2 * N)]
    rank = [i for i in range(1, 2 * N + 1)]
    for i in range(M):
        win = [0 for i in range(2 * N)]
        for j in range(N):
            if A[rank[2 * j] - 1][i] == A[rank[2 * j + 1] - 1][i]:
                win[rank[2 * j] - 1] += 1
                win[rank[2 * j + 1] - 1] += 1
            elif (A[rank[2 * j] - 1][i] == 'G' and A[rank[2 * j + 1] - 1][i] == 'C') or (A[rank[2 * j] - 1][i] == 'C' and A[rank[2 * j + 1] - 1][i] == 'P') or (A[rank[2 * j] - 1][i] == 'P' and A[rank[2 * j + 1] - 1][i] == 'G'):
                win[rank[2 * j] - 1] += 3
            else:
                win[rank[2 * j + 1] - 1] += 3
        rank = sorted(range(2 * N), key=lambda x: (-win[x], x))
        rank = [i + 1 for i in rank]
    for i in rank:
        print(i)
