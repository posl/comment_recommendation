def main():
    #入力
    n, m = map(int, input().split())
    #辺の数が0の時
    if m == 0:
        print(n)
        exit()
    #グラフの作成
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    #深さ優先探索
    def dfs(graph, start):
        stack = [start]
        seen = [False] * n
        seen[start] = True
        while stack:
            v = stack.pop()
            for i in graph[v]:
                if seen[i] == False:
                    stack.append(i)
                    seen[i] = True
        return seen.count(True)
    #連結成分の個数
    ans = 0
    for i in range(n):
        if dfs(graph, i) != 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()