def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    # print(H, W, S)
    S = [[0 if S[i][j] == '.' else -1 for j in range(W)] for i in range(H)]
    # print(S)
    def bfs(i, j):
        # print(i, j)
        que = [(i, j)]
        while que:
            i, j = que.pop(0)
            # print(i, j)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i+di < H and 0 <= j+dj < W and S[i+di][j+dj] == 0:
                    S[i+di][j+dj] = S[i][j] + 1
                    que.append((i+di, j+dj))
    for i in range(H):
        for j in range(W):
            if S[i][j] == 0:
                bfs(i, j)
    print(max([max(S[i]) for i in range(H)]))

if __name__ == '__main__':
    main()