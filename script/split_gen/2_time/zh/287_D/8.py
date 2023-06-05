def main():
    N, M = map(int, input().split())
    u, v = [], []
    for _ in range(M):
        u_i, v_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
    
    # 邻接表
    adj = [[] for _ in range(N)]
    for i in range(M):
        adj[u[i]-1].append(v[i]-1)
        adj[v[i]-1].append(u[i]-1)
    
    # 遍历
    for i in range(N):
        if len(adj[i]) > 2:
            print("No")
            return
        elif len(adj[i]) == 2:
            if adj[i][0] == adj[i][1]:
                print("No")
                return
        elif len(adj[i]) == 1:
            if i == 0 or i == N-1:
                print("No")
                return
            elif adj[i-1][0] == adj[i][0] or adj[i-1][0] == i or adj[i][0] == i+1:
                print("No")
                return
        elif len(adj[i]) == 0:
            if i != N-1:
                print("No")
                return
    print("Yes")
