def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    #友達関係
    friend = [[0 for _ in range(N)] for _ in range(N)]
    for a, b in AB:
        friend[a-1][b-1] = 1
        friend[b-1][a-1] = 1
    #ブロック関係
    block = [[0 for _ in range(N)] for _ in range(N)]
    for c, d in CD:
        block[c-1][d-1] = 1
        block[d-1][c-1] = 1
    #友達候補
    ans = [0 for _ in range(N)]
    for i in range(N):
        #自分自身と友達関係にある人数
        ans[i] = sum(friend[i]) - 1
        #ブロック関係にある人数
        for j in range(N):
            if block[i][j] == 1 and friend[i][j] == 1:
                ans[i] -= 1
    print(*ans)
