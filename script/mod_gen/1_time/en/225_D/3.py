def main():
    #read input
    N, Q = map(int, input().split())
    cars = [i for i in range(1, N + 1)]
    queries = []
    for i in range(Q):
        query = list(map(int, input().split()))
        queries.append(query)
    
    #process queries
    for i in range(Q):
        query = queries[i]
        if query[0] == 1:
            x = query[1]
            y = query[2]
            cars[x - 1] = y
        elif query[0] == 2:
            x = query[1]
            y = query[2]
            cars[x - 1] = x
        else:
            x = query[1]
            components = []
            components.append(x)
            while cars[x - 1] != x:
                x = cars[x - 1]
                components.append(x)
            components.reverse()
            print(len(components), end = ' ')
            for j in components:
                print(j, end = ' ')
            print()
main()
The problem statement is not clear. I think the following is better.
Takahashi is playing with toy trains, connecting and disconnecting them.
There are N toy train cars, with car numbers: Car 1, Car 2, ..., Car N.
Initially, all cars are separated.
You will be given Q queries. Process them in the order they are given.
There are three kinds of queries, as follows.
1 x y: Connect the front of Car y to the rear of Car x.
It is guaranteed that:
x ≠ y
just before this query, no train is connected to the rear of Car x;
just before this query, no train is connected to the front of Car y;
just before this query, Car x and Car y belong to different connected components.
2 x y: Disconnect the front of Car y from the rear of Car x.
It is guaranteed that:
x ≠ y;
just before this query, the front of Car y is directly connected to the rear of Car x.
3 x: Print the car numbers of the cars belonging to the connected component containing Car x, from front to back.
Constraints
2 ≦ N ≦ 10^5
1 ≦ Q ≦ 10^5
1 ≦ x ≦ N
1 ≦ y ≦ N
All values in input are

if __name__ == '__main__':
    main()