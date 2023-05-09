def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    #友達関係
    friend = [[0] * (N+1) for _ in range(N+1)]
    for a, b in AB:
        friend[a][b] = 1
        friend[b][a] = 1
    #ブロック関係
    block = [[0] * (N+1) for _ in range(N+1)]
    for c, d in CD:
        block[c][d] = 1
        block[d][c] = 1
    #友達候補
    ans = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if friend[i][j] == 1 and block[i][j] == 0:
                ans[i] += 1
    for i in range(1, N+1):
        ans[i] -= 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            if friend[i][j] == 1:
                ans[i] -= 1
                ans[j] -= 1
    for i in range(1, N+1):
        print(ans[i], end=" ")
