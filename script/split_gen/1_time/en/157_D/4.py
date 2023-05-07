def main():
    N, M, K = map(int, input().split())
    friends = [[0] * N for _ in range(N)]
    blocks = [[0] * N for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friends[A - 1][B - 1] = 1
        friends[B - 1][A - 1] = 1
    for _ in range(K):
        C, D = map(int, input().split())
        blocks[C - 1][D - 1] = 1
        blocks[D - 1][C - 1] = 1
    for i in range(N):
        blocks[i][i] = 1
    for i in range(N):
        for j in range(N):
            if friends[i][j] == 1:
                for k in range(N):
                    blocks[i][k] = 1
                    blocks[j][k] = 1
    for i in range(N):
        for j in range(N):
            if friends[i][j] == 1:
                blocks[i][j] = 0
    for i in range(N):
        print(sum(blocks[i]) - 1, end=' ')
    print()
