Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    par = [i for i in range(n+1)]
    rank = [0 for i in range(n+1)]
    size = [1 for i in range(n+1)]
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if rank[x] < rank[y]:
            par[x] = y
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1
        return True
    def same(x, y):
        return find(x) == find(y)
    def getsize(x):
        return size[find(x)]
    for i in range(q):
        c, x, y = map(int, input().split())
        if c == 1:
            unite(x, y)
        elif c == 2:
            unite(x, y)
        else:
            print(getsize(x), end = " ")
            for j in range(1, n+1):
                if same(x, j):
                    print(j, end = " ")
            print()

=======
Suggestion 2

def main():
    N, Q = map(int, input().sp

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    parent = [i for i in range(N+1)]
    size = [1 for i in range(N+1)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            y = query[2]
            parent[x] = y
            size[y] += size[x]
        elif query[0] == 2:
            x = query[1]
            y = query[2]
            parent[x] = x
            size[y] -= size[x]
        else:
            x = query[1]
            print(size[x], end=' ')
            for j in range(1, N+1):
                if parent[j] == x:
                    print(j, end=' ')
            print()
main()

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    anslist = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            pass
        elif query[0] == 2:
            pass
        else:
            anslist.append(query[1])
    print(anslist)
    return

=======
Suggestion 5

def main():
    #input
    n, q = map(int, input().split())
    #initialization
    c = [0]*q
    x = [0]*q
    y = [0]*q
    for i in range(q):
        c[i], x[i], y[i] = map(int, input().split())
    #solve
    #initialize
    par = [i for i in range(n+1)]
    siz = [1]*(n+1)
    #find
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    #unite
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if siz[x] < siz[y]:
            x, y = y, x
        siz[x] += siz[y]
        par[y] = x
    #same
    def same(x, y):
        return find(x) == find(y)
    #size
    def size(x):
        return siz[find(x)]
    #query
    for i in range(q):
        if c[i] == 1:
            unite(x[i], y[i])
        elif c[i] == 2:
            unite(x[i], y[i])
            siz[find(x[i])] -= 1
            siz[y[i]] += 1
            par[x[i]] = y[i]
        else:
            print(size(x[i]), end=' ')
            for j in range(1, n+1):
                if same(x[i], j):
                    print(j, end=' ')
            print()

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    # List of queries
    queries = []
    for i in range(Q):
        queries.append(list(map(int, input().split())))

    # List of cars
    cars = [i for i in range(1, N+1)]
    # List of connected components
    components = [[i] for i in range(1, N+1)]
    # List of car numbers of the front of connected components
    front = [i for i in range(1, N+1)]
    # List of car numbers of the rear of connected components
    rear = [i for i in range(1, N+1)]
    # List of car numbers of the rear of connected components
    rear = [i for i in range(1, N+1)]
    # Dictionary of car numbers of the front of connected components
    front_dict = {i: i for i in range(1, N+1)}
    # Dictionary of car numbers of the rear of connected components
    rear_dict = {i: i for i in range(1, N+1)}

    # Process each query
    for query in queries:
        # If query is type 1
        if query[0] == 1:
            # Get the car numbers
            x = query[1]
            y = query[2]
            # Get the front and rear of connected components
            front_x = front_dict[x]
            front_y = front_dict[y]
            rear_x = rear_dict[x]
            rear_y = rear_dict[y]
            # Get the index of connected components
            index_x = front.index(front_x)
            index_y = front.index(front_y)
            # Merge connected components
            components[index_x] = components[index_x] + components[index_y]
            # Update the front and rear of connected components
            front[index_x] = front_x
            rear[index_x] = rear_y
            # Update the front and rear of connected components
            front_dict[front_x] = front_x
            rear_dict[rear_y] = rear_y
            # Delete the front and rear of connected components
            front.pop(index_y)
            rear.pop(index_y)
            # Delete the front and rear of connected components
            del front_dict[front_y]
            del rear_dict[rear_y]
            # Delete the connected

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    #print("n: ", n)
    #print("q: ", q)
    #parent[i]: parent of i
    #parent[i] = i: i is root
    parent = list(range(n+1))
    #print("parent: ", parent)
    #size[i]: size of tree whose root is i
    size = [1]*(n+1)
    #print("size: ", size)
    #rank[i]: rank of i
    #rank[i] = 0: i is root
    #rank[i] = k: i is a child of the root of rank k-1 tree
    rank = [0]*(n+1)
    #print("rank: ", rank)
    #car[i]: car number of i
    car = list(range(n+1))
    #print("car: ", car)
    #ans: list of queries of the format 3 x
    ans = []
    #print("ans: ", ans)
    #print("query: ")
    for i in range(q):
        query = list(map(int, input().split()))
        #print(query)
        if len(query) == 2:
            ans.append(query)
        else:
            query[1] = car[query[1]]
            query[2] = car[query[2]]
            unite(query[1], query[2], parent, size, rank)
    #print("ans: ", ans)
    #print("parent: ", parent)
    #print("size: ", size)
    #print("rank: ", rank)
    #print("car: ", car)
    for query in ans:
        #print("query: ", query)
        x = query[1]
        #print("x: ", x)
        #print("parent: ", parent)
        #print("car: ", car)
        #print("parent[car[x]]: ", parent[car[x]])
        #print("parent[car[x]]: ", parent[car[x]])
        #print("car[parent[car[x]]]: ", car[parent[car[x]]])
        #print("car[parent[car[x]]]: ", car[parent[car[x]]])
        while parent[car[x]] != car[x]:
            x = parent[car[x]]
        #print("x: ", x)

=======
Suggestion 8

def main():
    #use sys.stdin.readline() instead of input()
    #to avoid TLE
    import sys
    n,q = map(int,sys.stdin.readline().split())
    train = [0]*n
    for i in range(n):
        train[i] = i+1
    for i in range(q):
        c,x,y = map(int,sys.stdin.readline().split())
        if c == 1:
            train[x-1] = train[y-1]
        elif c == 2:
            train[y-1] = y+1
        else:
            print(x,end=' ')
            temp = train[x-1]
            for j in range(x,n):
                if train[j] == temp:
                    print(j+1,end=' ')
            print()

=======
Suggestion 9

def main():
    #input
    N, Q = map(int, input().split())
    #The following 3 lists are used to store the information of the toy trains.
    #The i-th element of the list is the car number of the car connected to the rear of the i-th car.
    #If there is no car connected to the rear of the i-th car, the i-th element is 0.
    rear = [0] * N
    #The i-th element of the list is the car number of the car connected to the front of the i-th car.
    #If there is no car connected to the front of the i-th car, the i-th element is 0.
    front = [0] * N
    #The i-th element of the list is the car number of the car at the front of the connected component containing the i-th car.
    #If the i-th car is at the front of its connected component, the i-th element is i.
    front_of_component = [0] * N
    #The following 2 lists are used to store the information of the connected components.
    #The i-th element of the list is the number of cars in the connected component containing the i-th car.
    #If the i-th car is at the front of its connected component, the i-th element is the number of cars in the connected component.
    size_of_component = [0] * N
    #The i-th element of the list is the car number of the car at the front of the connected component containing the i-th car.
    #If the i-th car is at the front of its connected component, the i-th element is i.
    front_of_component = [0] * N
    #The following 2 lists are used to store the information of the connected components.
    #The i-th element of the list is the number of cars in the connected component containing the i-th car.
    #If the i-th car is at the front of its connected component, the i-th element is the number of cars in the connected component.
    size_of_component = [0] * N
    #The following 2 lists are used to store the information of the connected components.
    #The i-th element of the list is the number of cars in the connected component containing the i-th car.
    #If the i-th car is at the
