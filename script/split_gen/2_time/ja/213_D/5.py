def main():
    N = int(input())
    A = [0 for i in range(N-1)]
    B = [0 for i in range(N-1)]
    for i in range(N-1):
        A[i],B[i] = map(int, input().split())
    #隣接リストの作成
    G = [[] for i in range(N)]
    for i in range(N-1):
        G[A[i]-1].append(B[i]-1)
        G[B[i]-1].append(A[i]-1)
    #深さ優先探索
    visited = [False for i in range(N)]
    ans = []
    def dfs(v, pre):
        ans.append(v+1)
        visited[v] = True
        for i in range(len(G[v])):
            if not visited[G[v][i]]:
                dfs(G[v][i], v)
                ans.append(v+1)
        if v == 0:
            return
        else:
            ans.append(pre+1)
    dfs(0, 0)
    print(*ans)
