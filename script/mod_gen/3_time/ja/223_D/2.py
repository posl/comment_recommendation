def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
    # トポロジカルソート
    # 1. 入次数が 0 の頂点を取り出す
    # 2. その頂点から出ている辺を削除
    # 3. 1 に戻る
    # 4. 2 ができなくなったら終了
    # 入次数を数える
    in_deg = [0] * n
    for i in range(n):
        for j in graph[i]:
            in_deg[j] += 1
    # 入次数が 0 の頂点をスタックに追加
    stack = []
    for i in range(n):
        if in_deg[i] == 0:
            stack.append(i)
    # トポロジカルソート
    res = []
    while stack:
        v = stack.pop()
        res.append(v)
        for i in graph[v]:
            in_deg[i] -= 1
            if in_deg[i] == 0:
                stack.append(i)
    # グラフに閉路がある場合は -1 を出力する
    if len(res) != n:
        print(-1)
    else:
        print(*[r + 1 for r in res])

if __name__ == '__main__':
    main()