def solve():
    N,M = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(M)]
    edges.sort(key=lambda x:x[0])
    if len(edges) == 0:
        print("No")
        return
    if len(edges) == 1:
        print("Yes")
        return
    if len(edges) == 2:
        if edges[0][1] == edges[1][0]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(edges) == 3:
        if edges[0][1] == edges[1][0] and edges[1][1] == edges[2][0]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(edges) == 4:
        if edges[0][1] == edges[1][0] and edges[1][1] == edges[2][0] and edges[2][1] == edges[3][0]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(edges) == 5:
        if edges[0][1] == edges[1][0] and edges[1][1] == edges[2][0] and edges[2][1] == edges[3][0] and edges[3][1] == edges[4][0]:
            print("Yes")
            return
        else:
            print("No")
            return
    print("No")
    return
