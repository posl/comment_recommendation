def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    # 1. 隣接リストを作る
    # 2. 深さ優先探索で順番に訪れる都市を求める
    # 3. 1 が出てきたら終了
    # 隣接リストを作る
    adjList = [[] for _ in range(N+1)]
    for a, b in AB:
        adjList[a].append(b)
        adjList[b].append(a)
    # 深さ優先探索で順番に訪れる都市を求める
    visited = [False] * (N+1)
    visited[1] = True
    dfs(adjList, 1, visited, [1])
