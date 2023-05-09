def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        a,b = map(int,input().split())
        edges.append([a,b])
    #print(edges)
    #print("N",N)
    #print("edges",edges)
    #edges = [[1,2],[2,3],[2,4],[2,5],[4,7],[5,6],[6,8]]
    #edges = [[1,2],[2,3],[2,4],[2,5],[4,7],[5,6],[6,8]]
    colors = [0] * (N+1)
    color = 1
    for i in range(N-1):
        c = 1
        for j in range(2):
            if colors[edges[i][j]] == c:
                c += 1
        colors[edges[i][0]] = c
        colors[edges[i][1]] = c
        if color < c:
            color = c
    #print("colors",colors)
    print(color)
    for i in range(N-1):
        print(colors[edges[i][0]])
