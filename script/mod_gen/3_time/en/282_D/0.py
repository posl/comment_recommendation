def main():
    N, M = map(int, input().split())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    #print(N, M, u, v)
    edge = [[] for _ in range(N)]
    for i in range(M):
        edge[u[i]-1].append(v[i]-1)
        edge[v[i]-1].append(u[i]-1)
    #print(edge)
    ans = 0
    for i in range(N):
        for j in range(len(edge[i])):
            for k in range(j+1, len(edge[i])):
                if edge[i][j] in edge[edge[i][k]]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()