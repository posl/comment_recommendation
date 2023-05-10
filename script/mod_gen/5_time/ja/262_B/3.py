def main():
    N,M = map(int,input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if j in G[i]:
                for k in range(j+1,N):
                    if k in G[j] and i in G[k]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()