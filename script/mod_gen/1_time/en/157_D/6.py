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
    ans = [0] * N
    for i in range(N):
        ans[i] = N - 1 - sum(friends[i]) - sum(blocks[i])
    for i in range(N):
        for j in range(N):
            if friends[i][j] == 1 and blocks[i][j] == 1:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(N):
        if friends[i][i] == 1:
            ans[i] -= 1
    for i in range(N):
        print(ans[i], end=' ')
    print()

if __name__ == '__main__':
    main()