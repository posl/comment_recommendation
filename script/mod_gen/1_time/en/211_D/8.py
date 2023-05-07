def main():
    #read the input
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    #sort the input
    AB.sort(key=lambda x: x[0])
    #create a list of lists for the paths
    paths = [[] for _ in range(N)]
    for i in range(M):
        paths[AB[i][0] - 1].append(AB[i][1])
        paths[AB[i][1] - 1].append(AB[i][0])
    #create a list of lists for the distances
    dists = [[0 for _ in range(N)] for _ in range(N)]
    #create a list of lists for the counts
    counts = [[0 for _ in range(N)] for _ in range(N)]
    #initialize the first row of the counts
    counts[0] = [1 for _ in range(N)]
    #initialize the first row of the distances
    dists[0] = [1 for _ in range(N)]
    #initialize the visited list
    visited = [False for _ in range(N)]
    #initialize the queue
    queue = []
    #initialize the first element of the queue
    queue.append(1)
    #initialize the first element of the visited
    visited[0] = True
    #while the queue is not empty
    while queue:
        #get the next element
        node = queue.pop(0)
        #for each of the paths of the current node
        for i in range(len(paths[node - 1])):
            #if the node has not been visited
            if not visited[paths[node - 1][i] - 1]:
                #set the distance to the current node + 1
                dists[node - 1][paths[node - 1][i] - 1] = dists[node - 1][node - 1] + 1
                #set the count to the current node
                counts[node - 1][paths[node - 1][i] - 1] = counts[node - 1][node - 1]
                #set the visited flag to true
                visited[paths[node - 1][i] - 1] = True
                #add the node to the queue
                queue.append(paths[node

if __name__ == '__main__':
    main()