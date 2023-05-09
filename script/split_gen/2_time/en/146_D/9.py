def main():
    #N is the number of vertices
    N = int(input())
    #adjacency list
    adj = [[] for _ in range(N)]
    #colors
    colors = [0] * N
    #for each vertex
    for i in range(N-1):
        #a_i and b_i are two vertices that are connected by an edge
        a_i, b_i = map(int, input().split())
        #append b_i to adjacency list of a_i
        adj[a_i-1].append(b_i-1)
        #append a_i to adjacency list of b_i
        adj[b_i-1].append(a_i-1)
    #queue
    q = [0]
    #for each vertex
    for i in range(N):
        #color of i-th vertex
        color = 1
        #for each vertex j that is connected to i-th vertex
        for j in adj[i]:
            #if j-th vertex is already colored
            if colors[j] != 0:
                #if the color of j-th vertex is equal to the current color
                if colors[j] == color:
                    #increment the current color
                    color += 1
        #color the i-th vertex
        colors[i] = color
        #for each vertex j that is connected to i-th vertex
        for j in adj[i]:
            #if j-th vertex is not colored
            if colors[j] == 0:
                #append j-th vertex to the queue
                q.append(j)
    #print the number of colors used
    print(max(colors))
    #for each vertex
    for i in range(N-1):
        #print the color of the i-th edge
        print(colors[i])
