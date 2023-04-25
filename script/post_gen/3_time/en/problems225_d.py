Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    graph = [[] for i in range(N+1)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if len(query) == 3:
            graph[query[1]].append(query[2])
            graph[query[2]].append(query[1])
        elif len(query) == 2:
            graph[query[1]].remove(query[2])
            graph[query[2]].remove(query[1])
        elif len(query) == 1:
            visited = [False]*(N+1)
            visited[0] = True
            visited[query[0]] = True
            queue = [query[0]]
            print(len(graph[query[0]]), end=" ")
            while len(queue) > 0:
                current = queue.pop(0)
                for next in graph[current]:
                    if not visited[next]:
                        print(next, end=" ")
                        visited[next] = True
                        queue.append(next)
            print()

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    cars = [i for i in range(N + 1)]
    ans = []
    for i in range(Q):
        c, x, y = map(int, input().split())
        if c == 1:
            cars[x], cars[y] = cars[y], cars[x]
        elif c == 2:
            cars[x], cars[y] = cars[y], cars[x]
        else:
            ans.append(' '.join([str(cars.index(i)) for i in cars if i == x]))
    print('

'.join(ans))

=======
Suggestion 3

def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    from collections import deque
    N, Q = map(int, input().split())
    trains = [deque([i]) for i in range(N)]
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            c = trains[q[1]-1].popleft()
            trains[q[2]-1].appendleft(c)
        elif q[0] == 2:
            c = trains[q[1]-1].popleft()
            trains[q[2]-1].pop()
            trains[q[1]-1].appendleft(c)
        else:
            print(len(trains[q[1]-1]), end=' ')
            print(*trains[q[1]-1])
    return

=======
Suggestion 4

def main():
    N,Q = map(int,input().split())
    car = [i for i in range(N+1)]
    car[0] = -1
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            car[query[2]] = query[1]
        elif query[0] == 2:
            car[query[2]] = -1
        else:
            ans = []
            ans.append(query[1])
            while car[ans[-1]] != -1:
                ans.append(car[ans[-1]])
            print(len(ans),end=' ')
            print(*ans)

main()

=======
Suggestion 5

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

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    # 0: car number, 1: left, 2: right
    cars = [[i, None, None] for i in range(N+1)]
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            # connect y to x
            x = query[1]
            y = query[2]
            # find the rightmost car of x
            while cars[x][2]:
                x = cars[x][2]
            # find the leftmost car of y
            while cars[y][1]:
                y = cars[y][1]
            cars[x][2] = y
            cars[y][1] = x
        elif query[0] == 2:
            # disconnect y from x
            x = query[1]
            y = query[2]
            # find the rightmost car of x
            while cars[x][2]:
                x = cars[x][2]
            # find the leftmost car of y
            while cars[y][1]:
                y = cars[y][1]
            cars[x][2] = None
            cars[y][1] = None
        else:
            # print the car numbers of the connected component containing x
            x = query[1]
            # find the leftmost car of x
            while cars[x][1]:
                x = cars[x][1]
            # print the car numbers of the connected component
            ans = []
            while x:
                ans.append(x)
                x = cars[x][2]
            print(len(ans), ' '.join(map(str, ans)))

=======
Suggestion 7

def main():
    n,q = map(int,input()

=======
Suggestion 8

def main():
 N, Q = map(int, input().split())
 
 #parent[x] は、xの親の番号を格納する。親がいない場合は-(その集合のサイズ)
 #初期状態では、全てが根であるため、-1を代入する。
 parent = [-1] * N
 
 for _ in range(Q):
  c, x, y = map(int, input().split())
  x -= 1
  y -= 1
 
  if c == 1:
   unite(parent, x, y)
 
  elif c == 2:
   root_x = find_root(parent, x)
   root_y = find_root(parent, y)
   if root_x == root_y:
    parent[root_x] += 1
    parent[root_y] = x
 
  else:
   root_x = find_root(parent, x)
   root_y = find_root(parent, y)
   if root_x == root_y:
    print(size(parent, x))
    print(*sorted(connected_cars(parent, x)))
   else:
    print(0)

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    #N: number of cars
    #Q: number of queries
    
    #Initialize the list of cars
    #Each car is represented by a list of two elements: car number and the number of cars in the same connected component
    #The car number is the same as the index of the car in the list
    #The number of cars in the same connected component is 1 for each car initially
    cars = [[i, 1] for i in range(N)]
    
    #Initialize the list of queries
    queries = []
    for i in range(Q):
        query = list(map(int, input().split()))
        queries.append(query)
    
    #Initialize the list of connected components
    #Each connected component is represented by a list of car numbers
    #Initially, there are N connected components
    connected_components = [[i] for i in range(N)]
    
    #Process the queries
    for query in queries:
        #If the query is of the format 1 x y
        if query[0] == 1:
            x = query[1]
            y = query[2]
            
            #Get the car numbers of the cars in the connected component containing Car x
            x_cc = cars[x-1][0]
            x_cc_car_numbers = connected_components[x_cc]
            
            #Get the car numbers of the cars in the connected component containing Car y
            y_cc = cars[y-1][0]
            y_cc_car_numbers = connected_components[y_cc]
            
            #Get the number of cars in the connected component containing Car x
            x_cc_num_cars = len(x_cc_car_numbers)
            
            #Get the number of cars in the connected component containing Car y
            y_cc_num_cars = len(y_cc_car_numbers)
            
            #Update the car numbers of the cars in the connected component containing Car x
            for car_number in y_cc_car_numbers:
                cars[car_number][0] = x_cc
            
            #Update the number of cars in the connected component containing Car x
            cars[x-1][1] += y_cc_num_cars
            
            #Update the number of cars in the connected component containing Car y
            cars[y-1][1] = 1
            
            #Update the list of connected components
            x_cc_car_numbers.extend

=======
Suggestion 10

def main():
    # get input
    n, q = map(int, input().split())
    # make a list of lists to hold the trains
    trains = []
    # make a list to hold the car numbers
    car_nums = []
    # make a list to hold the car numbers that are connected to the rear
    rear_nums = []
    # make a list to hold the car numbers that are connected to the front
    front_nums = []
    # make a list to hold the car numbers that are connected to the rear and front
    both_nums = []
    # make a list to hold the car numbers that are not connected to the rear or front
    neither_nums = []
    # make a list to hold the car numbers that are connected to the rear and front
    both_nums = []
    # make a list to hold the car numbers that are not connected to the rear or front
    neither_nums = []
    # fill the trains list with n empty lists
    for i in range(n):
        trains.append([])
    # fill the car_nums list with the car numbers
    for i in range(n):
        car_nums.append(i+1)
    # fill the rear_nums list with the car numbers that are connected to the rear
    for i in range(n):
        rear_nums.append(i+1)
    # fill the front_nums list with the car numbers that are connected to the front
    for i in range(n):
        front_nums.append(i+1)
    # fill the both_nums list with the car numbers that are connected to the rear and front
    for i in range(n):
        both_nums.append(i+1)
    # fill the neither_nums list with the car numbers that are not connected to the rear or front
    for i in range(n):
        neither_nums.append(i+1)
    # make a list to hold the queries
    queries = []
    # fill the queries list with the queries
    for i in range(q):
        queries.append(list(map(int, input().split())))
    # process the queries
    for query in queries:
        # check the first value of the query
        if query[0] == 1:
            # make a list to hold the car numbers in the rear_nums list
            temp = []
            # make a list to hold the car numbers in the front_nums list
            temp2 = []
            # make a list to
