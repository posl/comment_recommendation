def main():
    n,q = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(n-1)]
    cd = [list(map(int, input().split())) for i in range(q)]
    g = [[] for i in range(n+1)]
    for a,b in ab:
        g[a].append(b)
        g[b].append(a)
    d = [-1]*(n+1)
    d[1] = 0
    q = [1]
    while q:
        qq = []
        for p in q:
            for np in g[p]:
                if d[np] == -1:
                    d[np] = d[p] + 1
                    qq.append(np)
        q = qq
    for c,d in cd:
        if (d - c) % 2 == 0:
            print('Town')
        else:
            print('Road')
