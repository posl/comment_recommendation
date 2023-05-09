def main():
    #入力
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    P = list(map(int, input().split()))
    #グラフの連結成分の数
    visited = [False] * 9
    def dfs(v):
        visited[v] = True
        for w in G[v]:
            if not visited[w]:
                dfs(w)
    cnt = 0
    for i in range(9):
        if not visited[i]:
            dfs(i)
            cnt += 1
    #グラフの連結成分の数が2以上なら、不可能
    if cnt > 1:
        print(-1)
        return
    #グラフの連結成分の数が1なら、必要な操作回数は、頂点に置かれたコマの数
    ans = 0
    for i in range(8):
        if P[i] != i + 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()