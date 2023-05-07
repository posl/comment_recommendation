def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        g = [[] for _ in range(N)]
        for j in range(M):
            if i == j:
                continue
            a,b = AB[j]
            a,b = a-1,b-1
            g[a].append(b)
        for j in range(N):
            q = [j]
            v = [0]*N
            while q:
                x = q.pop()
                for y in g[x]:
                    if v[y]:
                        continue
                    v[y] = 1
                    q.append(y)
            ans += sum(v)
    print(ans)
