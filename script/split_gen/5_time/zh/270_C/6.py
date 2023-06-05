def main():
    n, x, y = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    edges.sort()
    print(edges)
    #print(edges)
    #for i in range(n-1):
    #    if edges[i][0] == x and edges[i][1] == y:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][0] == x:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == y:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][0] == y:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == x:
    #        print(edges[i][0], edges[i][1])
    #    else:
    #        continue
    #print(edges)
    #for i in range(n-1):
    #    if edges[i][0] == x:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == y:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == x:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][0] == y:
    #        print(edges[i][0], edges[i][1])
    #    else:
    #        continue
    #print(edges)
    #for i in range(n-1):
    #    if edges[i][0] == x:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][0] == y:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == x:
    #        print(edges[i][0], edges[i][1])
    #    elif edges[i][1] == y:
    #        print(edges[i][0], edges[i][1])
    #    else:
    #        continue
    #print(edges)
    #for i in range(n-1):
    #    if edges[i][1] == x:
    #        print(edges[i][0
