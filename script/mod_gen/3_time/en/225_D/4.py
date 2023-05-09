def main():
    N, Q = map(int, input().split())
    #parent[i] is the parent of i
    parent = [i for i in range(N+1)]
    #size[i] is the number of nodes in the connected component containing i
    size = [1 for i in range(N+1)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            #connect the front of Car y to the rear of Car x
            #it is guaranteed that x ≠ y
            #just before this query, no train is connected to the rear of Car x
            #just before this query, no train is connected to the front of Car y
            #just before this query, Car x and Car y belong to different connected components
            #find the root of x
            x = query[1]
            while parent[x] != x:
                x = parent[x]
            #find the root of y
            y = query[2]
            while parent[y] != y:
                y = parent[y]
            if x != y:
                #if x and y are not in the same connected component, connect them
                parent[y] = x
                size[x] += size[y]
        elif query[0] == 2:
            #disconnect the front of Car y from the rear of Car x
            #it is guaranteed that x ≠ y
            #just before this query, the front of Car y is directly connected to the rear of Car x
            #find the root of y
            y = query[2]
            while parent[y] != y:
                y = parent[y]
            #disconnect y from its parent
            parent[y] = y
            size[parent[query[1]]] -= size[y]
        else:
            #print the car numbers of the cars belonging to the connected component containing Car x, from front to back
            #find the root of x
            x = query[1]
            while parent[x] != x:
                x = parent[x]
            print(size[x], end = ' ')
            #print the car numbers of the cars belonging to the connected component containing x
            for j in range(1, N+1):
                if parent[j] == x:
                    print(j, end = ' ')
            print('')

if __name__ == '__main__':
    main()