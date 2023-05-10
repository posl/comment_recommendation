def main():
    N = int(input())
    edges = []
    for i in range(0, N-1):
        edges.append(list(map(int, input().split())))
    
    #print(edges)
    #print(N)
    
    # color[v] = 0 or 1
    color = [-1] * (N+1)
    color[1] = 0
    
    # bfs
    queue = [1]
    while len(queue) > 0:
        #print(queue)
        v = queue.pop(0)
        #print(v)
        for edge in edges:
            if edge[0] == v:
                #print(edge[1])
                if color[edge[1]] == -1:
                    color[edge[1]] = (color[edge[0]] + edge[2]) % 2
                    queue.append(edge[1])
            elif edge[1] == v:
                #print(edge[0])
                if color[edge[0]] == -1:
                    color[edge[0]] = (color[edge[1]] + edge[2]) % 2
                    queue.append(edge[0])
            else:
                continue
    #print(color)
    for c in color[1:]:
        print(c)

if __name__ == '__main__':
    main()