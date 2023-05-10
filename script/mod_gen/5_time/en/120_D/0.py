def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #print(N, M)
    #print(A)
    #print(B)
    # create a list of lists
    # each element is a list of bridges connected to that island
    # the index of the list is the island number
    # the list of bridges is a list of indices in the A and B lists
    # we use indices instead of the actual bridge numbers to save space
    # the list of bridges is sorted by bridge number
    # we could use a set instead of a list, but we would have to convert it to a list before sorting it
    # we could use a dictionary instead of a list, but we would have to convert it to a list before sorting it
    island_connections = [[] for i in range(N+1)]
    for i in range(M):
        island_connections[A[i]].append(i)
        island_connections[B[i]].append(i)
    #print(island_connections)
    # create a list of bridges
    # each element is a list of islands connected to that bridge
    # the index of the list is the bridge number
    # the list of islands is a list of indices in the A and B lists
    # we use indices instead of the actual island numbers to save space
    # the list of islands is sorted by island number
    # we could use a set instead of a list, but we would have to convert it to a list before sorting it
    # we could use a dictionary instead of a list, but we would have to convert it to a list before sorting it
    bridge_connections = [[] for i in range(M)]
    for i in range(M):
        bridge_connections[i].append(A[i])
        bridge_connections[i].append(B[i])
    #print(bridge_connections)
    # create a list of bridges that have been removed
    # each element is a list of bridges that have been removed
    # the index of the list is the number of bridges that have been removed
    # the list of bridges is a list of indices in the A and B lists
    # we use indices instead of the actual bridge numbers to save space
    # the

if __name__ == '__main__':
    main()