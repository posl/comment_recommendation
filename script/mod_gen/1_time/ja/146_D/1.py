def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    c = [0]*N
    def dfs(v,p,cnt):
        for i in G[v]:
            if i == p:
                continue
            cnt += 1
            c[i] = cnt
            dfs(i,v,cnt)
    dfs(0,-1,0)
    print(max(c)+1)
    for i in range(N-1):
        print(c[i+1]+1)

if __name__ == '__main__':
    main()