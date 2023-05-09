def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    #print(edges)
    colors = [0] * (N-1)
    #print(colors)
    #print(edges[0][0])
    #print(edges[0][1])
    #print(edges[1][0])
    #print(edges[1][1])
    #print(edges[2][0])
    #print(edges[2][1])
    #print(edges[3][0])
    #print(edges[3][1])
    for i in range(N-1):
        if edges[i][0] == 1:
            colors[i] = edges[i][1]
        elif edges[i][1] == 1:
            colors[i] = edges[i][0]
    #print(colors)
    #print(colors[0])
    #print(colors[1])
    #print(colors[2])
    #print(colors[3])
    #print(colors[4])
    #print(colors[5])
    print(max(colors))
    for i in range(N-1):
        print(colors[i])
