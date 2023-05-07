def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    #print(N)
    #print(edges)
    colors = [0] * (N-1)
    #print(colors)
    for i in range(N-1):
        #print(i)
        #print(edges[i])
        #print(edges[i][0])
        #print(edges[i][1])
        #print(colors)
        if colors[edges[i][0]-1] == 0:
            colors[edges[i][0]-1] = 1
        if colors[edges[i][1]-1] == 0:
            colors[edges[i][1]-1] = 1
        if colors[edges[i][0]-1] == colors[edges[i][1]-1]:
            colors[edges[i][1]-1] += 1
    #print(colors)
    print(max(colors))
    for i in range(N-1):
        print(colors[i])
