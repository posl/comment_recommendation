def solve():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    sign = [0]*N
    sign[0] = -1
    que = [0]
    while que:
        v = que.pop()
        for w in edge[v]:
            if sign[w] == 0:
                que.append(w)
                sign[w] = v+1
    if 0 in sign[1:]:
        print("No")
    else:
        print("Yes")
        for s in sign[1:]:
            print(s)
solve()
